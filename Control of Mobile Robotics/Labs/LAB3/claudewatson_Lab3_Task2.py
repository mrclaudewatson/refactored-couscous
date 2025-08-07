from fairis_tools.my_robot import MyRobot
import math

robot = MyRobot()

robot.load_environment('/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze6.xml')
timestep = int(robot.getBasicTimeStep())
robot.move_to_start()

dt = 0.032
integral = integral2 = angleIntegral = rIntegral = 0
previousError = previousError2 = previousAngleError = rPrevError = 0

cameraMid = robot.rgb_camera.getWidth() / 2


# def distanceToGoal(goal_x, goal_y):
#     gpsX, gpsY, _ = robot.gps.getValues()
#     return math.sqrt((goal_x - gpsX) ** 2 + (goal_y - gpsY) ** 2)


# def orientation_to_goal(goal_x, goal_y):
#     gpsX, gpsY, _ = robot.gps.getValues()
#     goal_angle = math.atan2(goal_y - gpsY, goal_x - gpsX)
#     current_orientation = math.radians(robot.get_compass_reading())
#     orientation_error = (goal_angle - current_orientation + math.pi) % (2 * math.pi) - math.pi
#     return orientation_error


def centered(actualX, frameX):
    if abs(actualX - frameX) < 2:
        return True
    else:
        return False


def saturation(speed):
    if speed >= robot.max_motor_velocity:
        speed = robot.max_motor_velocity
    elif speed <= -robot.max_motor_velocity:
        speed = -robot.max_motor_velocity

    return speed


def rotate(radianAngle):
    # Calculate the necessary rotation based on the angle in radians
    if radianAngle < 0:
        robot.set_left_motors_velocity(-1.5)
        robot.set_right_motors_velocity(1.5)
    else:
        robot.set_left_motors_velocity(1.5)
        robot.set_right_motors_velocity(-1.5)

    # Initialize the starting position
    initialPos = robot.get_compass_reading()

    while robot.step(timestep) != -1:
        currentPos = robot.get_compass_reading()

        # Check if the desired rotation has been achieved
        if abs((currentPos - initialPos + 180) % 360 - 180) >= abs(math.degrees(radianAngle)):
            # Stop the motors after achieving the desired angle
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)
            break


# def computeDistanceAndOrientation(goal):
#     goalOrientation = math.degrees(goal.getOrientation()[2])
#     robotOrientation = robot.get_compass_reading()

#     xPos, yPos, zPos = goal.getPosition()[0], goal.getPosition()[1], goal.getPosition()[2]

#     robotPosX, robotPosY, robotPosZ = robot.gps.getValues()[0], robot.gps.getValues()[1], robot.gps.getValues()[2]
#     print(f"Goal Orientation: {goalOrientation}\nGoal Position: X = {xPos}, Y= {yPos}\n\nRobot Position: X = {robotPosX}, Y = {robotPosY}")


#     distance = math.sqrt(((xPos - robotPosX) ** 2) + ((yPos - robotPosY) ** 2))
#     print(f"Distance: {distance}")



def forwardPID():

    global previousError2, integral2

    Kp = 2
    Kd = 0.0
    Ki = 0

    actualDistance = min(robot.get_lidar_range_image()[390:410])
    if actualDistance > 100:
        return 5

    desiredDistance = 0

    # calculating the error
    error = actualDistance - desiredDistance

    # P
    P = Kp * error

    # I
    integral2 += error * dt
    I = integral2 * Ki

    # D
    derivative = (error - previousError2) / dt
    D = derivative * Kd

    # updating the previous error
    previousError2 = error

    speed2 = P + I + D

    return saturation(speed2)


def centerPID(PosX):
    global integral, previousError

    Kp = 0.035
    Ki = 0.0
    Kd = 0.00

    desired = cameraMid

    error = desired - PosX

    # P
    P = Kp * error

    # I
    integral += error * dt
    I = integral * Ki

    # D
    derivative = (error - previousError) / dt
    D = derivative * Kd

    # updating the previous error
    previousError = error

    speed = P + I + D

    print(f"CENTER P:{P}, I:{I}, D:{D}")
    print(f"Center Speed: {speed}")


    return abs(saturation(speed))


def motionToGoal():

    recObjects = robot.rgb_camera.getRecognitionObjects()

    # if theres an object detected
    if len(recObjects) > 0:

        goal = recObjects[0]

        # get position on image
        x1 = goal.getPositionOnImage()[0]
        print(f"Position on Image: {x1}")
        
        # computeDistanceAndOrientation(goal)

        maxThreshold = robot.rgb_camera.getWidth() / 2 + 1
        minThreshold = robot.rgb_camera.getWidth() / 2 - 1

        # if it is not centered
        if not centered(x1, cameraMid):
            speed = centerPID(x1)
            if x1 < 320:
                robot.set_left_motors_velocity(-speed)
                robot.set_right_motors_velocity(speed)
            if x1 > 320:
                robot.set_left_motors_velocity(speed)
                robot.set_right_motors_velocity(-speed)
        # if it is centered
        else:
            speed2 = forwardPID()
            robot.set_left_motors_velocity(speed2)
            robot.set_right_motors_velocity(speed2)
        
        if robot.get_lidar_range_image()[400] < 0.51:
            print(f"Robot stopped. \nDistance: {round(robot.get_lidar_range_image()[400], 3)} meters.")
            robot.stop()


def wallPID(wall):

    global previousAngleError, angleIntegral

    Kp = 1.5 # 1, 1.25, 1.5
    Ki = 0 # 0.00005
    Kd = 10 # 5-10

    # getting distances from the wall, both left and right
    leftDistance = min(robot.get_lidar_range_image()[200:390])
    rightDistance = min(robot.get_lidar_range_image()[410:600])

    desiredDistance = 0.4

    if wall == "R":
        error = rightDistance - desiredDistance
    else: 
        error = leftDistance - desiredDistance

    P = Kp * error

    angleIntegral += error * dt
    I = angleIntegral * Ki

    derivative = (error - previousAngleError) / dt
    D = Kd * derivative

    previousAngleError = error

    angularVelocity = P + I + D

    return saturation(angularVelocity)


def wallFollow(wall):

    leftDistance = min(robot.get_lidar_range_image()[200:390])
    rightDistance = min(robot.get_lidar_range_image()[410:600])

    maintain = 0.4  # Desired distance to the wall

    # Linear velocity to approach or move along the wall
    linearVelocity = forwardPID()
    angularVelocity = wallPID(wall)

    linearVelocity = saturation(linearVelocity)
    angularVelocity = saturation(angularVelocity)

    # Adjust the speeds based on the proximity to the wall
    if wall == "R":
        if rightDistance < maintain:
            # Turn left if too close to the right wall
            Rspeed = linearVelocity + abs(angularVelocity)
            Lspeed = linearVelocity - abs(angularVelocity)
        elif rightDistance > maintain:
            # Turn right if too far from the right wall
            Rspeed = linearVelocity - abs(angularVelocity)
            Lspeed = linearVelocity + abs(angularVelocity)
        else:
            # Move forward if at the correct distance
            Rspeed = linearVelocity
            Lspeed = linearVelocity
    else:
        if leftDistance < maintain:
            # Turn right if too close to the left wall
            Rspeed = linearVelocity - abs(angularVelocity)
            Lspeed = linearVelocity + abs(angularVelocity)
        elif leftDistance > maintain:
            # Turn left if too far from the left wall
            Rspeed = linearVelocity + abs(angularVelocity)
            Lspeed = linearVelocity - abs(angularVelocity)
        else:
            # Move forward if at the correct distance
            Rspeed = linearVelocity
            Lspeed = linearVelocity

    # Ensure speeds don't exceed the motor limits
    Rspeed = saturation(Rspeed)
    Lspeed = saturation(Lspeed)

    return Rspeed, Lspeed


if __name__ == "__main__":
    while robot.step(timestep) != -1:

        wall = "L"

        recObjects = robot.rgb_camera.getRecognitionObjects()

        frontDistance = robot.get_lidar_range_image()[400]

        leftDistance = min(robot.get_lidar_range_image()[200:390])
        rightDistance = min(robot.get_lidar_range_image()[410:600])
        
        print(f"-"*50)
        print(f"Front Distance: {round(frontDistance, 2)}")
        print(f"Left Distance: {round(leftDistance, 2)}")
        print(f"Right Distance: {round(rightDistance, 2)}")

        # If object found, approach the goal
        if len(recObjects) > 0: 
            goal = recObjects[0]
            motionToGoal()

        else:
            
            # When wall ahead is closer than 0.4m, initiate wall-following
            if frontDistance < 0.45:
                if wall == "R":
                    rotate(-math.pi/2)  # Rotate left

                else:
                    rotate(math.pi/2)   # Rotate right
                # After rotation, begin wall-following
                Rspeed, Lspeed = wallFollow(wall)
                robot.set_left_motors_velocity(Lspeed)
                robot.set_right_motors_velocity(Rspeed)
                # if theres a wall directly infront of robot while wall following, rotate 90 degrees


            # If no object is detected but still approaching the wall (0.4m < frontDistance < 1.0m)
            elif frontDistance < 1.23:
                # Move forward to get closer to the wall before initiating wall-following
                speed2 = forwardPID()
                robot.set_left_motors_velocity(speed2)
                robot.set_right_motors_velocity(speed2)

            else:
                # Regular wall-following behavior when wall is not too close or object isn't seen
                Rspeed, Lspeed = wallFollow(wall)
                robot.set_left_motors_velocity(Lspeed)
                robot.set_right_motors_velocity(Rspeed)
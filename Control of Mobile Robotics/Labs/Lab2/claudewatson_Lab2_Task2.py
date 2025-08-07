from fairis_tools.my_robot import MyRobot
import math

robot = MyRobot()
maze4 = '/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze4.xml'
maze3 = '/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze3.xml'
robot.load_environment(maze4)
timestep = int(robot.getBasicTimeStep())
robot.move_to_start()

dt = 0.032

previousError = 0
integral = 0

previousAngleError = 0
angleIntegral = 0

rIntegral = 0
rPrevError = 0

initialX = 2
initialY = -2 
prevEncoder = 0
radius = 0.043

# PID controller to move forward
def PID():

    global previousError, integral

    Kp = 2
    Ki = 0
    Kd = 0

    actualDistance = robot.get_lidar_range_image()[400]
    desiredDistance = 0

    # calculating the error
    error = actualDistance - desiredDistance

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

    return speed


# PID controller to move along the side walls
def wallPID(wall):

    global previousAngleError, angleIntegral

    Kp = 2.5 # 1, 1.25, 1.5
    Ki = 0.0001 # 0.00005
    Kd = 9 # 5-10

    # getting distances from the wall, both left and right
    leftDistance = min(robot.get_lidar_range_image()[200:390])
    rightDistance = min(robot.get_lidar_range_image()[410:600])
    print("Left Distance: ", leftDistance)
    print("Right Distance: ", rightDistance)

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

    return angularVelocity


def updatePosition():
    global initialX, initialY, prevEncoder, radius

    # Get the angle the robot is facing in degrees
    theta = robot.get_compass_reading()

    # Store the encoder readings
    encoderVal = robot.get_encoder_readings()

    # Get the four wheels' encoder readings and store them separately
    currEncoder = (encoderVal[0] + encoderVal[1] + encoderVal[2] + encoderVal[3]) / 4

    # Convert the angle to radians
    angleRadians = math.radians(theta)

    # Calculate the distance traveled 
    distanceTravelled = (currEncoder - prevEncoder) * radius

    # Update the (x) horizontal and (y) vertical positions
    initialX += distanceTravelled * math.cos(angleRadians)
    initialY += distanceTravelled * math.sin(angleRadians)

    # Print the x, y, and theta values
    print("x=", round(initialX, 1), end=" ")
    print("y=", round(initialY, 1), end=" ")
    print("Theta=", theta)

    # Update the previous encoder value for next calculation
    prevEncoder = currEncoder


def rotate(radianAngle):
    # Calculate the necessary rotation based on the angle in radians
    if radianAngle < 0:
        robot.set_left_motors_velocity(-1)
        robot.set_right_motors_velocity(1)
    else:
        robot.set_left_motors_velocity(1)
        robot.set_right_motors_velocity(-1)

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


def saturation(speed):
    if speed >= robot.max_motor_velocity:
        speed = robot.max_motor_velocity
    elif speed <= -robot.max_motor_velocity:
        speed = -robot.max_motor_velocity

    return speed


def wallFollow(wall):

    leftDistance = robot.get_lidar_range_image()[200]
    rightDistance = robot.get_lidar_range_image()[600]

    maintain = 0.4

    linearVelocity = PID()
    angularVelocity = wallPID(wall)

    linearVelocity = saturation(linearVelocity)
    angularVelocity = saturation(angularVelocity)

    if wall == "R":
        if rightDistance < maintain:
            Rspeed = linearVelocity + abs(angularVelocity)
            Lspeed = linearVelocity - abs(angularVelocity)
        elif rightDistance > maintain:
            Rspeed = linearVelocity - abs(angularVelocity)
            Lspeed = linearVelocity + abs(angularVelocity)
        else:
            Rspeed = linearVelocity
            Lspeed = linearVelocity
    else:
        if leftDistance < maintain:
            Rspeed = linearVelocity - abs(angularVelocity)
            Lspeed = linearVelocity + abs(angularVelocity)
        elif leftDistance > maintain:
            Rspeed = linearVelocity + abs(angularVelocity)
            Lspeed = linearVelocity - abs(angularVelocity)
        else:
            Rspeed = linearVelocity
            Lspeed = linearVelocity
    
    # print("Right wheel speed: ", Rspeed)
    # print("Left wheel speed: ", Lspeed)

    return Rspeed, Lspeed

def goal():
    global initialX, initialY
    targetX = -1
    targetY = 1
    range = 0.5

    if (targetX - range <= initialX <= targetX + range) and (targetY - range <= initialY <= targetY + range):
        robot.stop()
        time = robot.getTime()
        print("Total Time: ", round(time, 2))
        return True
    return False



# main loop
if __name__ == "__main__":
    while robot.step(timestep) != -1:

        wall = "R"
        Rspeed, Lspeed = wallFollow(wall)

        robot.set_left_motors_velocity(Lspeed)
        robot.set_right_motors_velocity(Rspeed)

        updatePosition()

        if goal():
            break

        frontDistance = robot.get_lidar_range_image()[400]
        # print("Front Distance: ", frontDistance)
        print("*" * 50)

        if frontDistance < 0.45 and wall == "R":
            rotate(-math.pi/2)
        elif frontDistance < 0.45 and wall == "L":
            rotate(math.pi/2)
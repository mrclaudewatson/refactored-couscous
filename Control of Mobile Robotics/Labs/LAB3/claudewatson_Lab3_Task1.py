from fairis_tools.my_robot import MyRobot
import math

robot = MyRobot()

robot.load_environment('/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze5.xml')
timestep = int(robot.getBasicTimeStep())
robot.move_to_start()

dt = 0.032
integral = integral2 = 0
previousError = previousError2 = 0

cameraMid = robot.rgb_camera.getWidth() / 2


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

    return saturation(speed)


def forwardPID():

    global previousError2, integral2

    Kp = 2
    Kd = 0.01
    Ki = 0.01

    actualDistance = min(robot.get_lidar_range_image()[390:410])
    desiredDistance = 0.5

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


def motionToGoal():

    recObjects = robot.rgb_camera.getRecognitionObjects()

    # if theres an object detected
    if len(recObjects) > 0:

        goal = recObjects[0]

        # get position on image
        x1 = goal.getPositionOnImage()[0]
        print(f"Position on Image: {x1}")

        maxThreshold = robot.rgb_camera.getWidth() / 2 + 1
        minThreshold = robot.rgb_camera.getWidth() / 2 - 1

        # if it is not centered
        if not centered(x1, cameraMid):
            speed = centerPID(x1)/2
            robot.set_left_motors_velocity(-speed)
            robot.set_right_motors_velocity(speed)

        # if it is centered
        else:
            # if it is centered but out of range from the lidar sensor
            # it moves forward to get within the lidar range
            if  minThreshold < x1 < maxThreshold:
                if min(robot.get_lidar_range_image()[390:410]) > 100:
                    robot.set_left_motors_velocity(9)
                    robot.set_right_motors_velocity(9)
                # once it is in the lidar range, switch to PID controlled velocities
                # based on distance from goal
                else: 
                    speed2 = forwardPID()/2
                    speed = centerPID(x1)/2
                    if x1 < 325:
                        robot.set_left_motors_velocity((speed2 - speed))
                        robot.set_right_motors_velocity((speed2 + speed))
                        print(f"Speed: {speed2}")
                    elif x1 > 315:
                        robot.set_left_motors_velocity((speed2 + speed))
                        robot.set_right_motors_velocity((speed2 - speed))
                        print(f"Speed: {speed2}")
                    else:
                        robot.set_left_motors_velocity(speed2)
                        robot.set_right_motors_velocity(speed2)
                        print(f"Speed: {speed2}")                        


if __name__ == "__main__":
    while robot.step(timestep) != -1:

        recObjects = robot.rgb_camera.getRecognitionObjects()

        if len(recObjects) == 0:
            # rotate robot to find object
            print(f"Finding Object...")
            robot.set_left_motors_velocity(-5)
            robot.set_right_motors_velocity(5)

        elif len(recObjects) > 0: 
            print(f"Object found! Moving to target")
            motionToGoal()

            print("Front Distance: ", round(min(robot.get_lidar_range_image()[390:410]), 2))
            print(f"--------------------------------------------")

        if robot.get_lidar_range_image()[400] < 0.51:
            print("Goal reached!\nDistance from goal: ", round(robot.get_lidar_range_image()[400], 2))
            robot.stop()
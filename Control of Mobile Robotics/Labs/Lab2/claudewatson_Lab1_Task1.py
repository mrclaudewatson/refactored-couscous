from fairis_tools.my_robot import MyRobot
import math

robot = MyRobot()

maze_file = '/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze2.xml'
robot.load_environment(maze_file)

timestep = int(robot.getBasicTimeStep())

robot.move_to_start()

dt = 0.032

# defining PID variables
Kp = 2
Ki = 0
Kd = 0

previousError = 0
integral = 0

# PID controller
def PID():

    global previousError, integral
    actualDistance = robot.get_lidar_range_image()[400]
    desiredDistance = 1.0

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



# function to cap the velocities at the respective max and minimum values
def saturation(speed):
    if speed >= robot.max_motor_velocity:
        speed = robot.max_motor_velocity
    elif speed <= -robot.max_motor_velocity:
        speed = -robot.max_motor_velocity

    return speed



if __name__ == "__main__":
    while robot.step(timestep) != -1:
        print("Distance: ", robot.get_lidar_range_image()[400])
    
        velocity = PID()

        speed = saturation(velocity)

        robot.set_right_motors_velocity(speed)
        robot.set_left_motors_velocity(speed)
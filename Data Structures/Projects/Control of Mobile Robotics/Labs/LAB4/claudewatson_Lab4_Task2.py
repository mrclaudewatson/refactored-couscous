from fairis_tools.my_robot import MyRobot
from math import exp, sqrt, pi
import math

robot = MyRobot()

robot.load_environment('/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze8.xml')
timestep = int(robot.getBasicTimeStep())
robot.move_to_start()


# function to return robot to inital direction
def fixDirection(initialDirection):

    # Get the current heading
    currDirection = robot.get_compass_reading()

    # Calculate the shortest rotation direction and angle
    angleDifference = (initialDirection - currDirection + math.pi) % (2 * math.pi) - math.pi

    # Determine rotation direction and set motor speeds
    if angleDifference > 0:
        rotationSpeed = 3
    else:
        rotationSpeed = -3

    robot.set_left_motors_velocity(-rotationSpeed)
    robot.set_right_motors_velocity(rotationSpeed)

    # Rotate until aligned with the initial heading
    while abs(angleDifference) > 0.01:  # Small margin for precision
        robot.step(timestep)
        currDirection = robot.get_compass_reading()
        angleDifference = (initialDirection - currDirection + math.pi) % (2 * math.pi) - math.pi

        # Adjust rotation direction dynamically in case angleDifference changes sign
        if angleDifference > 0 and rotationSpeed < 0:
            robot.set_left_motors_velocity(-3)
            robot.set_right_motors_velocity(3)

        elif angleDifference < 0 and rotationSpeed > 0:
            robot.set_left_motors_velocity(3)
            robot.set_right_motors_velocity(-3)

    # Stop the robot after alignment
    robot.set_left_motors_velocity(0)
    robot.set_right_motors_velocity(0)



def facingNorth():
    if 100 > robot.get_compass_reading() > 80:
        return True
    else:
        return False


def faceNorth():
    while not (92.5 > robot.get_compass_reading() > 87.5):
        rotate(math.pi/50)


def rotate(radianAngle):
    robot.set_left_motors_velocity(0)
    robot.set_right_motors_velocity(0)
    
    if radianAngle < 0:
        robot.set_left_motors_velocity(-3)
        robot.set_right_motors_velocity(3)
    else:
        robot.set_left_motors_velocity(3)
        robot.set_right_motors_velocity(-3)

    initialPos = robot.get_compass_reading()

    while robot.step(timestep) != -1:
        currentPos = robot.get_compass_reading()

        if abs((currentPos - initialPos + 180) % 360 - 180) >= abs(math.degrees(radianAngle)):
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)
            break


def encoderReading():
    return robot.wheel_radius * robot.get_front_left_motor_encoder_reading()


def moveToNextCell(distance):

    prev_encoder = encoderReading()
    while robot.step(timestep) != -1:
        current_encoder = encoderReading()
        if current_encoder >= prev_encoder + distance:
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)
            break
        robot.set_left_motors_velocity(5)
        robot.set_right_motors_velocity(5)


def takeLidarReadings():

    lidar_readings = {
        'N': robot.get_lidar_range_image()[400],  # Simulated LiDAR reading for the North direction
        'E': robot.get_lidar_range_image()[600],  # Simulated LiDAR reading for the East direction
        'S': robot.get_lidar_range_image()[0],  # Simulated LiDAR reading for the South direction
        'W': robot.get_lidar_range_image()[200]   # Simulated LiDAR reading for the West direction
    }
    # Convert distances to wall presence (True for wall, False for no wall)
    wall_threshold = 1.0  # Example: Walls detected within 0.5 meters
    wall_config = {direction: distance <= wall_threshold for direction, distance in lidar_readings.items()}
    return wall_config


cellStructure = {

    1: {'W': True, 'N': True, 'E': False, 'S': False},
    2: {'W': False, 'N': True, 'E': False, 'S': True},
    3: {'W': False, 'N': True, 'E': False, 'S': True},
    4: {'W': False, 'N': True, 'E': False, 'S': True},
    5: {'W': False, 'N': True, 'E': True, 'S': False},

    6: {'W': True, 'N': False, 'E': True, 'S': False},
    7: {'W': True, 'N': True, 'E': False, 'S': True},
    8: {'W': False, 'N': True, 'E': False, 'S': True},
    9: {'W': False, 'N': True, 'E': False, 'S': True},
    10: {'W': False, 'N': False, 'E': True, 'S': True},

    11: {'W': True, 'N': False, 'E': False, 'S': False},
    12: {'W': False, 'N': True, 'E': False, 'S': True},
    13: {'W': False, 'N': True, 'E': False, 'S': True},
    14: {'W': False, 'N': True, 'E': False, 'S': True},
    15: {'W': False, 'N': True, 'E': False, 'S': False},

    16: {'W': True, 'N': False, 'E': False, 'S': False},
    17: {'W': False, 'N': True, 'E': False, 'S': True},
    18: {'W': False, 'N': True, 'E': False, 'S': True},
    19: {'W': False, 'N': True, 'E': False, 'S': True},
    20: {'W': False, 'N': False, 'E': True, 'S': False},

    21: {'W': True, 'N': False, 'E': False, 'S': True},
    22: {'W': False, 'N': True, 'E': False, 'S': True},
    23: {'W': False, 'N': True, 'E': False, 'S': True},
    24: {'W': False, 'N': True, 'E': False, 'S': True},
    25: {'W': False, 'N': False, 'E': True, 'S': True},

}


# def calculateProbabilities():

#     # Step 1: Take LiDAR readings (observed walls)
#     observed_walls = takeLidarReadings()

#     # Step 2: Initialize probabilities for all cells
#     probabilities = {}

#     # Step 3: Define sensor model probabilities
#     match_prob = 0.9  # Probability when z == s (match)
#     mismatch_prob = 0.1  # Probability when z != s (mismatch)

#     # Step 4: Calculate probabilities for each cell
#     for cell, walls in cellStructure.items():
#         cell_probability = 1.0  # Start with a neutral probability

#         for direction in ['N', 'E', 'S', 'W']:
#             if observed_walls[direction] == walls[direction]:
#                 cell_probability *= match_prob  # Multiply by match probability
#             else:
#                 cell_probability *= mismatch_prob  # Multiply by mismatch probability

#         probabilities[cell] = cell_probability

#     # Step 5: Normalize probabilities
#     total_probability = sum(probabilities.values())
#     if total_probability > 0:
#         probabilities = {cell: prob / total_probability for cell, prob in probabilities.items()}

#     # Step 6: Find the cell with the highest probability
#     highest_prob_cell = max(probabilities, key=probabilities.get)
#     highest_prob_value = probabilities[highest_prob_cell]

#     # Step 7: Print probabilities and the highest probability cell
#     print("\nCell Probabilities:")
#     for cell, prob in sorted(probabilities.items()):
#         print(f"Cell {cell}: {prob:.4f}")

#     print(f"\nMost likely cell: {highest_prob_cell} with probability {highest_prob_value:.4f}")


def calculateProbabilities():
    """
    Calculate and print the probabilities of all 25 cells based on the sensor model.
    If multiple cells have the same highest probability, print them.
    """

    # Step 1: Take LiDAR readings (observed walls)
    observed_walls = takeLidarReadings()

    # Step 2: Initialize probabilities for all cells
    probabilities = {}

    # Step 3: Define sensor model probabilities
    match_prob = 0.9  # Probability when z == s (match)
    mismatch_prob = 0.1  # Probability when z != s (mismatch)

    # Step 4: Calculate probabilities for each cell
    for cell, walls in cellStructure.items():
        cell_probability = 1.0  # Start with a neutral probability

        for direction in ['N', 'E', 'S', 'W']:
            if observed_walls[direction] == walls[direction]:
                cell_probability *= match_prob  # Multiply by match probability
            else:
                cell_probability *= mismatch_prob  # Multiply by mismatch probability

        probabilities[cell] = cell_probability

    # Step 5: Normalize probabilities
    total_probability = sum(probabilities.values())
    if total_probability > 0:
        probabilities = {cell: prob / total_probability for cell, prob in probabilities.items()}

    # Step 6: Find the highest probability and cells with the same value
    highest_prob_value = max(probabilities.values())
    highest_prob_cells = [cell for cell, prob in probabilities.items() if prob == highest_prob_value]

    # Step 7: Print probabilities and the highest probability cell(s)
    print("\nCell Probabilities:")
    for cell, prob in sorted(probabilities.items()):
        print(f"Cell {cell}: {prob:.4f}")

    if len(highest_prob_cells) > 1:
        print(f"\nCells with the same highest probabilities ({highest_prob_value:.4f}): {', '.join(map(str, highest_prob_cells))}")
    else:
        print(f"\nMost likely cell: {highest_prob_cells[0]} with probability {highest_prob_value:.4f}")


if __name__ == "__main__":
    visited_cells = 0  # Counter to track the number of cells visited

    while robot.step(timestep) != -1:
        if visited_cells >= 15:  # Stop after 15 cells
            print("Visited 15 cells. Stopping the robot.")
            break

        print(f"*" * 33)
        currDirection = robot.get_compass_reading()
        faceNorth()
        observed_walls = takeLidarReadings()

        # Probability calculation and output
        calculateProbabilities()

        for direction, has_wall in observed_walls.items():
            wall_status = "Wall" if has_wall else "No Wall"

        fixDirection(currDirection)

        if robot.get_lidar_range_image()[400] < 1 and robot.get_lidar_range_image()[200] < 1 and robot.get_lidar_range_image()[600] < 1:
            rotate(math.pi)
        elif robot.get_lidar_range_image()[400] < 1 and robot.get_lidar_range_image()[200] < 1:
            rotate(math.pi / 2)
        elif robot.get_lidar_range_image()[400] < 1 and robot.get_lidar_range_image()[600] < 1:
            rotate(-math.pi / 2)
        elif robot.get_lidar_range_image()[400] < 1:
            rotate(math.pi / 2)

        moveToNextCell(1)
        visited_cells += 1  # Increment the counter after moving forward

        print(f"Cells visited: {visited_cells}")

from fairis_tools.my_robot import MyRobot
from math import exp, sqrt, pi
import math
import matplotlib.pyplot as plt

robot = MyRobot()

robot.load_environment('/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze7.xml')
timestep = int(robot.getBasicTimeStep())
robot.move_to_start()

cylinderRadius = 0.25

calculated_positions = []
gps_positions = []

calcedDistance = {
    
    1: {"distances": {"red": 4.53, "green": 4.53, "blue": 6.36}, "visited": False},
    2: {"distances": {"red": 3.54, "green": 4.74, "blue": 5.70}, "visited": False},
    3: {"distances": {"red": 2.55, "green": 5.15, "blue": 5.15}, "visited": False},
    4: {"distances": {"red": 1.58, "green": 5.70, "blue": 4.74}, "visited": False},
    5: {"distances": {"red": 0.71, "green": 6.36, "blue": 4.53}, "visited": False},
    6: {"distances": {"red": 4.74, "green": 3.54, "blue": 5.70}, "visited": False},
    7: {"distances": {"red": 3.81, "green": 3.81, "blue": 4.95}, "visited": False},
    8: {"distances": {"red": 2.92, "green": 4.30, "blue": 4.30}, "visited": False},
    9: {"distances": {"red": 2.12, "green": 4.95, "blue": 3.81}, "visited": False},
    10: {"distances": {"red": 1.58, "green": 5.70, "blue": 3.54}, "visited": False},
    11: {"distances": {"red": 5.15, "green": 2.55, "blue": 5.15}, "visited": False},
    12: {"distances": {"red": 4.30, "green": 2.92, "blue": 4.30}, "visited": False},
    13: {"distances": {"red": 3.54, "green": 3.54, "blue": 3.54}, "visited": False},
    14: {"distances": {"red": 2.92, "green": 4.30, "blue": 2.92}, "visited": False},
    15: {"distances": {"red": 2.55, "green": 5.15, "blue": 2.55}, "visited": False},
    16: {"distances": {"red": 5.70, "green": 1.58, "blue": 4.74}, "visited": False},
    17: {"distances": {"red": 4.95, "green": 2.12, "blue": 3.81}, "visited": False},
    18: {"distances": {"red": 4.30, "green": 2.92, "blue": 2.92}, "visited": False},
    19: {"distances": {"red": 3.81, "green": 3.81, "blue": 2.12}, "visited": False},
    20: {"distances": {"red": 3.54, "green": 4.74, "blue": 1.58}, "visited": False},
    21: {"distances": {"red": 6.36, "green": 0.71, "blue": 4.53}, "visited": False},
    22: {"distances": {"red": 5.70, "green": 1.58, "blue": 3.54}, "visited": False},
    23: {"distances": {"red": 5.15, "green": 2.55, "blue": 2.55}, "visited": False},
    24: {"distances": {"red": 4.74, "green": 3.54, "blue": 1.58}, "visited": False},
    25: {"distances": {"red": 4.53, "green": 4.53, "blue": 0.71}, "visited": False}
}


def gaussian(mu,s):
    sigma = 1
    coefficient = 1 / (sqrt(2 * pi * sigma ** 2))
    exponent = -((s - mu) ** 2) / (2 * sigma ** 2)
    probability = coefficient * exp(exponent)
    return probability


def trilateration(x1, y1, r1, x2, y2, r2, x3, y3, r3):

    A1 = 2 * (-x1 + x2)
    B1 = 2 * (-y1 + y2)
    C1 = (r1 ** 2) - (r2 ** 2) - (x1 ** 2) + (x2 ** 2) - (y1 ** 2) + (y2 ** 2)

    A2 = 2 * (-x2 + x3)
    B2 = 2 * (-y2 + y3)
    C2 = (r2 ** 2) - (r3 ** 2) - (x2 ** 2) + (x3 ** 2) - (y2 ** 2) + (y3 ** 2)

    x = ((C1 * B2) - (C2 * B1)) / ((B2 * A1) - (B1 * A2))
    y = ((C1 * A2) - (A1 * C2)) / ((B1 * A2) - (A1 * B2))

    # Get GPS coordinates
    gpsX, gpsY, _ = robot.gps.getValues()

    # Append positions for plotting
    calculated_positions.append((x, y))
    gps_positions.append((gpsX, gpsY))

    # Print both positions for comparison
    print(f"Trilateration: Calculated Position: (x: {x:.3f}, y: {y:.3f})")
    print(f"GPS: Actual Position: (x: {gpsX:.3f}, y: {gpsY:.3f})")

    return x, y


def rotate(radianAngle):

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


def scanLandmarks():

    initialDirection = robot.get_compass_reading()

    redFlag = greenFlag = blueFlag = 0
    measuredDistances = {}

    # Start rotating the robot
    robot.set_left_motors_velocity(-3)
    robot.set_right_motors_velocity(3)

    while robot.step(timestep) != -1:
        recObjects = robot.rgb_camera.getRecognitionObjects()

        # Process recognized objects
        for cylinder in recObjects:
            colors = cylinder.getColors()
            position = cylinder.getPosition()

            # Ignore yellow landmarks
            if colors[0] == 1 and colors[1] == 1:
                continue

            # Identify the landmark color and compute distance
            if colors[0] == 1 and "red" not in measuredDistances:
                measuredDistances["red"] = position[0] + cylinderRadius
                redFlag = 1

            elif colors[1] == 1 and "green" not in measuredDistances:
                measuredDistances["green"] = position[0] + cylinderRadius
                greenFlag = 1

            elif colors[2] == 1 and "blue" not in measuredDistances:
                measuredDistances["blue"] = position[0] + cylinderRadius
                blueFlag = 1

        if redFlag == 1 and greenFlag == 1 and blueFlag == 1:
            # Stop the robot after the scan
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)

            fixDirection(initialDirection)

            return measuredDistances


def markCellVisited(cellId, calcedDistance):
    if cellId is not None and cellId in calcedDistance:
        calcedDistance[cellId]["visited"] = True


def calculateProbabilities(measuredDistances, calcedDistance):

    maxProb = 0
    mostLikelyCell = None

    for cellId, data in calcedDistance.items():
        # Skip visited cells
        if data["visited"]:
            continue

        # Calculate combined probability for the cell
        cellProb = 1
        for color, precomputed_distance in data["distances"].items():
            if color in measuredDistances:
                measured = measuredDistances[color]
                precomputed = precomputed_distance
                cellProb *= gaussian(measured, precomputed)

        # Track the cell with the highest probability
        if cellProb > maxProb:
            maxProb = cellProb
            mostLikelyCell = cellId

    print(f"-" * 75)

    print(f"Most likely cell: {mostLikelyCell} with probability: {round(maxProb, 3)}")
    return mostLikelyCell


def moveToCell1():

    while robot.get_lidar_range_image()[400] > 1.0:  
        moveToNextCell(1.0)

    rotate(-math.pi / 2)

    while robot.get_lidar_range_image()[400] > 1.0:  
        moveToNextCell(1.0)

    # # Step 4: Confirm the robot is in cell 1
    # print("Re-scanning landmarks to verify position...")
    # measuredDistances = scanLandmarks()
    # mostLikelyCell = calculateProbabilities(measuredDistances, calcedDistance)

    rotate(-math.pi/2)


def plot_positions():
    """
    Plots the calculated positions vs. GPS positions.
    """
    # Extract x and y for calculated and GPS positions
    calculated_x = [pos[0] for pos in calculated_positions]
    calculated_y = [pos[1] for pos in calculated_positions]
    gps_x = [pos[0] for pos in gps_positions]
    gps_y = [pos[1] for pos in gps_positions]

    # Create a scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(calculated_x, calculated_y, color='blue', label='Calculated Positions')
    plt.scatter(gps_x, gps_y, color='red', label='GPS Positions', marker='x')

    # Add labels, legend, and title
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Comparison of Calculated and GPS Positions')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


if __name__ == "__main__":

    moveToCell1()

    while any(not data["visited"] for data in calcedDistance.values()):
        print(f"*"*50)

        measuredDistances = scanLandmarks()
        mostLikelyCell = calculateProbabilities(measuredDistances, calcedDistance)

        if mostLikelyCell is not None:
            # print(f"Robot is most likely in cell {mostLikelyCell}")
            markCellVisited(mostLikelyCell, calcedDistance)

        x1, y1, r1 = 2.5, 2.5, measuredDistances.get("red", 0)
        x2, y2, r2 = -2.5, -2.5, measuredDistances.get("green", 0)
        x3, y3, r3 = 2.5, -2.5, measuredDistances.get("blue", 0)

        # Calculate and compare positions
        trilateration(x1, y1, r1, x2, y2, r2, x3, y3, r3)    


        # Step 2.2: Check for walls and navigate
        front_distance = robot.get_lidar_range_image()[400]

        # If there's a wall ahead
        if front_distance < 1.0:

            if not any(not data["visited"] for data in calcedDistance.values()):
                break

            currHeading = robot.get_compass_reading()

            # If facing north, turn right; if south, turn left
            if 100 > currHeading > 80:  # Facing north
                rotate(math.pi / 2)
                moveToNextCell(1.0)
                rotate(math.pi / 2)

            elif 285 > currHeading > 255:  # Facing south
                rotate(-math.pi / 2)
                moveToNextCell(1.0)
                rotate(-math.pi / 2)

        else:
            # No wall, move forward to the next cell
            moveToNextCell(1.0)

    # Step 3: Final Results
    print("ALL CELLS VISITED")
    plot_positions()





# if __name__ == "__main__":
#     visited_cells = set()  # Set to store unique cell positions

#     while robot.step(timestep) != -1:
#         if len(visited_cells) >= 15:  # Stop after 15 unique cells
#             print("15 CELLS VISITED")
#             break

#         print(f"*" * 75)
#         currDirection = robot.get_compass_reading()
#         faceNorth()
#         observed_walls = takeLidarReadings()

#         # Probability calculation and output
#         calculateProbabilities()

#         for direction, has_wall in observed_walls.items():
#             wall_status = "Wall" if has_wall else "No Wall"
#             print(f"  {direction}: {wall_status}")

#         fixDirection(currDirection)

#         if robot.get_lidar_range_image()[400] < 1 and robot.get_lidar_range_image()[200] < 1 and robot.get_lidar_range_image()[600] < 1:
#             rotate(math.pi)
#         elif robot.get_lidar_range_image()[400] < 1 and robot.get_lidar_range_image()[200] < 1:
#             rotate(math.pi / 2)
#         elif robot.get_lidar_range_image()[400] < 1 and robot.get_lidar_range_image()[600] < 1:
#             rotate(-math.pi / 2)
#         elif robot.get_lidar_range_image()[400] < 1:
#             rotate(math.pi / 2)

#         moveToNextCell(1)

#         # Step 5: Track the robot's position and update visited cells
#         gpsX, gpsY, _ = robot.gps.getValues()  # Get the current GPS position
#         current_position = (round(gpsX), round(gpsY))  # Round to avoid floating-point errors
#         visited_cells.add(current_position)  # Add the position to the set

#         print(f"Cells visited: {len(visited_cells)}")

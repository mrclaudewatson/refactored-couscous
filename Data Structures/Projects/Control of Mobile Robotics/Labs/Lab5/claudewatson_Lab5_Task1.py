from fairis_tools.my_robot import MyRobot
import numpy as np
from collections import deque
import math

# Initialize robot
robot = MyRobot()
robot.load_environment('/Users/claudewatson/FAIRIS-Lite/WebotsSim/worlds/Fall24/maze8.xml')
timestep = int(robot.getBasicTimeStep())
robot.move_to_start()

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
    15: {'W': False, 'N': True, 'E': True, 'S': False},

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

# Helper function to get encoder reading for distance
def encoderReading():
    return robot.wheel_radius * robot.get_front_left_motor_encoder_reading()

# Rotate function
def rotate(radianAngle):
    robot.set_left_motors_velocity(0)
    robot.set_right_motors_velocity(0)

    if radianAngle < 0:
        robot.set_left_motors_velocity(-1.5)
        robot.set_right_motors_velocity(1.5)
    else:
        robot.set_left_motors_velocity(1.5)
        robot.set_right_motors_velocity(-1.5)

    initialPos = robot.get_compass_reading()

    while robot.step(timestep) != -1:
        currentPos = robot.get_compass_reading()
        if abs((currentPos - initialPos + 180) % 360 - 180) >= abs(math.degrees(radianAngle)):
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)
            break

# Move forward based on distance
def moveToNextCell(distance):
    prev_encoder = encoderReading()
    while robot.step(timestep) != -1:
        current_encoder = encoderReading()
        if current_encoder >= prev_encoder + distance - 0.005:  # Add small tolerance
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)
            break
        robot.set_left_motors_velocity(5.5)
        robot.set_right_motors_velocity(5.5)

# Robot Navigator Class
class MyRobotNavigator:
    def __init__(self, robot, cell_size=1, grid_size=5):
        self.robot = robot
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.x = 0
        self.y = 0
        self.theta = 0
        self.current_cell = None

    def initialize_pose(self):
        start_pos = self.robot.starting_position
        self.x = start_pos.x
        self.y = start_pos.y
        self.theta = self.robot.get_compass_reading()
        self.current_cell = self.coords_to_cell(self.x, self.y)
        self.print_pose()

    def coords_to_cell(self, x, y):
        col = int(x + 2)
        row = int(2 - y)
        return row * self.grid_size + col + 1

    def print_pose(self):
        print(f"s = ({self.x:.1f}, {self.y:.1f}, {self.current_cell}, {self.theta:.1f}°)")

    def update_pose(self):
        self.theta = self.robot.get_compass_reading()
        encoder_distance = encoderReading()
        self.x += encoder_distance * np.cos(np.radians(self.theta))
        self.y += encoder_distance * np.sin(np.radians(self.theta))
        self.current_cell = self.coords_to_cell(self.x, self.y)
        self.print_pose()

    def turn(self, angle):
        radian_angle = math.radians(angle)
        rotate(radian_angle)

    def move_forward(self, distance):
        moveToNextCell(distance)
        robot.set_left_motors_velocity(0) 
        robot.set_right_motors_velocity(0)

    def move_to_cell(self, target_cell):
        if self.current_cell == target_cell:
            return

        target_x, target_y = self.cell_to_coords(target_cell)
        current_x, current_y, current_theta = self.x, self.y, self.theta

        dx = target_x - current_x
        dy = target_y - current_y

        # Determine the desired direction (North, East, South, West)
        if dx == 0 and dy > 0:
            desired_theta = 90  # North
        elif dx > 0 and dy == 0:
            desired_theta = 0  # East
        elif dx == 0 and dy < 0:
            desired_theta = 270  # South
        elif dx < 0 and dy == 0:
            desired_theta = 180  # West
        
        current_theta = current_theta % 360
        desired_theta = desired_theta % 360

        turn_angle = (current_theta - desired_theta) % 360  
        if turn_angle > 180: 
            turn_angle -= 360

        self.turn(turn_angle)

        distance = self.cell_size
        self.move_forward(distance)

        self.x, self.y = target_x, target_y
        self.theta = desired_theta
        self.current_cell = target_cell
        self.print_pose()  

    def cell_to_coords(self, cell):
        row = (cell - 1) // self.grid_size
        col = (cell - 1) % self.grid_size
        x = -2 + col 
        y = 2 - row
        return (x, y)

    def calculate_turn_angle(self, current_theta, target_x, target_y, current_x, current_y):
        dx = target_x - current_x
        dy = target_y - current_y
        target_theta = np.degrees(np.arctan2(dy, dx))
        angle_to_turn = (target_theta - current_theta) % 360
        if angle_to_turn > 180:
            angle_to_turn -= 360
        return angle_to_turn


# Wavefront Planner Class
class MazeNavigator:
    def __init__(self, cell_structure, grid_size=5):
        self.cell_structure = cell_structure
        self.grid_size = grid_size
        self.wavefront = None
        self.start_cell = None
        self.goal_cell = None

    def set_start_and_goal(self, start, goal):
        self.start_cell = start
        self.goal_cell = goal

    def initialize_wavefront(self):
        self.wavefront = np.full((self.grid_size, self.grid_size), np.inf)
        goal_coords = self.cell_to_coords(self.goal_cell)
        self.wavefront[goal_coords] = 0

    def cell_to_coords(self, cell):
        row = (cell - 1) // self.grid_size
        col = (cell - 1) % self.grid_size
        return (row, col)

    def coords_to_cell(self, row, col):
        return row * self.grid_size + col + 1

    def calculate_wavefront(self):
        queue = deque([self.cell_to_coords(self.goal_cell)])  # Start from the goal
        while queue:
            current = queue.popleft()
            current_value = self.wavefront[current]
            cell = self.coords_to_cell(*current)

            # Directions: N, S, W, E
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            walls = ['N', 'S', 'W', 'E']  # Wall directions
            neighbor_walls = ['S', 'N', 'E', 'W']  # Opposite walls for neighbors

            for idx, (dr, dc) in enumerate(directions):
                nr, nc = current[0] + dr, current[1] + dc  # Neighbor coordinates
                if 0 <= nr < self.grid_size and 0 <= nc < self.grid_size:
                    neighbor_cell = self.coords_to_cell(nr, nc)

                    current_wall = self.cell_structure[cell][walls[idx]]
                    neighbor_wall = self.cell_structure[neighbor_cell][neighbor_walls[idx]]

                    if (not current_wall and not neighbor_wall):  # No walls blocking
                        neighbor_coords = (nr, nc)
                        if self.wavefront[neighbor_coords] > current_value + 1:  # Unvisited or higher value
                            self.wavefront[neighbor_coords] = current_value + 1
                            queue.append(neighbor_coords)


    def find_path(self):
        start_coords = self.cell_to_coords(self.start_cell)
        goal_coords = self.cell_to_coords(self.goal_cell)

        current_coords = start_coords
        path = []

        while current_coords != goal_coords:
            row, col = current_coords
            path.append(self.coords_to_cell(row, col))  # Append cell number to the path
            current_value = self.wavefront[row, col]    # Access wavefront value at (row, col)

            # Directions: N, S, W, E
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            walls = ['N', 'S', 'W', 'E']  # Wall directions
            neighbor_walls = ['S', 'N', 'E', 'W']  # Opposite walls for neighbors

            found_next = False  # Flag to track if a valid next cell is found

            for idx, (dr, dc) in enumerate(directions):
                nr, nc = row + dr, col + dc  # Neighbor coordinates
                if 0 <= nr < self.grid_size and 0 <= nc < self.grid_size:
                    neighbor_cell = self.coords_to_cell(nr, nc)

                    current_wall = self.cell_structure[self.coords_to_cell(row, col)][walls[idx]]
                    neighbor_wall = self.cell_structure[neighbor_cell][neighbor_walls[idx]]

                    if (not current_wall and not neighbor_wall
                        and self.wavefront[nr, nc] == current_value - 1):
                        current_coords = (nr, nc)  # Move to the neighbor
                        found_next = True
                        break

            if not found_next:
                raise ValueError(f"Pathfinding failed: No valid neighbor found from cell {self.coords_to_cell(row, col)}")

        # Append the goal cell to the path
        path.append(self.goal_cell)
        return path


    def navigate_path(self, robot_navigator):
        path = self.find_path()
        print(f"Path: {' → '.join(map(str, path))}")
        for cell in path:
            robot_navigator.move_to_cell(cell)
        print("Goal Reached!")


if __name__ == "__main__":
    # Grab the initial random starting position
    start_pos = robot.starting_position
    x = start_pos.x
    y = start_pos.y
    theta = math.degrees(start_pos.theta)

    # Initialize maze navigator
    maze_navigator = MazeNavigator(cellStructure)
    robot_navigator = MyRobotNavigator(robot)

    # Determine the current cell and goal based on the starting position
    current_cell = robot_navigator.coords_to_cell(x, y)
    goal_cell = 7

    print(f"Starting Position: x = {x:.2f}, y = {y:.2f}, θ = {theta:.2f}°, cell = {current_cell}")
    robot_navigator.initialize_pose()  # Initialize the robot's pose

    # Set the start and goal cells
    maze_navigator.set_start_and_goal(start=current_cell, goal=goal_cell)

    maze_navigator.initialize_wavefront()
    maze_navigator.calculate_wavefront()
    path = maze_navigator.find_path()

    # Print the computed path
    print(f"Computed Path: {' → '.join(map(str, path))}")

    for cell in path:
        print(f"-"*96)

        print(f"Navigating to cell: {cell}")
        robot_navigator.move_to_cell(cell)  # Move to each cell in the path
        if cell == 7:
            print(f"CELL 7 REACHED, STOPPING ROBOT")
            robot.set_left_motors_velocity(0)
            robot.set_right_motors_velocity(0)
            robot.stop()
            break
        print(f"Reached cell: {cell}")
How to Run

-- Configuration Instructions --

### Screen Settings
- Open the `utils.h` file.
- Update the screen width and height variables.
- The program will dynamically adjust the grid size to fit the screen while maintaining the aspect ratio.

### Grid Customization
- Navigate to the `grid.h` file.
- Define the dimensions of the grid by setting the number of squares.
- Configure the number of walls and markers; these will be placed randomly on the grid.

-- Other Information --

### Objective
The robot is programmed to search for the shortest path to the nearest marker, retrieve it, and return to its home base. This process is repeated until the robot collects all markers on the grid.

### Starting Position
- Set the robot's initial location and facing direction using the command prompt window with the following format: 
  - `row column direction`
  - Rows and columns start from 0.
  - Direction can be `north`, `east`, `south`, or `west`.
  - Example: `0 0 north` places the robot in the top-left corner facing north.

### Termination Condition
- If no accessible path to any marker exists, the robot will not move, and the program will terminate.
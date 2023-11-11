-- HOW TO RUN --

Update the 'utils.h' to adjust the screen width and height. The program will automatically adjust the size of the grid to fit the screen, while still maintaining the aspect ratio.

Inside of 'grid.h' you can adjust how many squares the grid consists off. You can also specify the number of walls and markers that will be randomly placed on the grid.

The robot will find the shortest path to the nearest marker, pick it up, and return back to its home. The robot will then repeat this process until all markers have been collected.

You can set the location and direction of the robot's starting position in this format: row (starting from 0) column (starting from 0) direction (north, east, south west). For example, 0 0 north will place the robot in the top left corner facing north. You do this from inside of the command prompt window.

If there is no path to any markers, the robot will not move, and the program will end.
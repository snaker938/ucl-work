#include <stdio.h>
#include <stdlib.h>
#include "grid.h"
#include "graphics.h"
#include "utils.h"
#include <string.h>

int main(int argc, char **argv)
{
    setWindowSize(WIN_WIDTH, WIN_HEIGHT);

    // The default values if the command line arguments are not given.
    int initialX = 0;
    int initialY = 0;
    char *initialDirection = "north";

    int numericalDirection;

    if (argc == 4) // Four arguments were typed
    {
        initialX = atoi(argv[1]);   // Get x value
        initialY = atoi(argv[2]);   // Get y value
        initialDirection = argv[3]; // Get direction

        // Convert the direction to a number
        if (strcmp(initialDirection, "north") == 0)
        {
            numericalDirection = 0;
        }
        else if (strcmp(initialDirection, "west") == 0)
        {
            numericalDirection = 1;
        }
        else if (strcmp(initialDirection, "south") == 0)
        {
            numericalDirection = 2;
        }
        else if (strcmp(initialDirection, "east") == 0)
        {
            numericalDirection = 3;
        }
        else
        {
            return 0;
        }
    }

    // Call the drawRobot function with the parsed arguments
    initialiseGrid(initialX, initialY, numericalDirection);

    return 0;
}

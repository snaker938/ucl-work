#include <stdio.h>
#include <stdlib.h>
#include "grid.h"
#include "graphics.h"
#include "utils.h"
#include <string.h>

int main(int argc, char **argv)
{
    // Set window size using defined constants.
    setWindowSize(WIN_WIDTH, WIN_HEIGHT);

    // Default values for initial position and direction.
    int initialX = 0, initialY = 0, numericalDirection = 0;
    char *initialDirection = "north";

    // Update initial position and direction if command line arguments are provided.
    if (argc == 4)
    {
        initialX = atoi(argv[1]);
        initialY = atoi(argv[2]);
        initialDirection = argv[3];

        // Map direction string to a numerical value.
        if (strcmp(initialDirection, "west") == 0)
            numericalDirection = 1;
        else if (strcmp(initialDirection, "south") == 0)
            numericalDirection = 2;
        else if (strcmp(initialDirection, "east") == 0)
            numericalDirection = 3;
        // "north" remains the default (0), so no need to check for it.
    }

    // Initialize grid with the provided or default position and direction.
    initialiseGrid(initialX, initialY, numericalDirection);

    return 0; // Exit program.
}

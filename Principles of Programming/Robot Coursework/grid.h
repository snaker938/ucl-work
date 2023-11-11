#ifndef GRID_H
#define GRID_H

// Define the grid properties and marker placement
#define GRID_WIDTH 10
#define GRID_HEIGHT 10

#define WALL_COUNT 20
#define MARKER_COUNT 10

struct Node
{
    int distance;
    int visited;
    int wall;
    int marker;
    int home;
    int previousNode[2];
    int robot;
    int x;
    int y;
};

extern struct Node grid[GRID_WIDTH][GRID_HEIGHT];

// Function prototypes for managing the grid and its elements
void initialiseGrid(int startX, int startY, int startDirection);

#endif /* GRID_H */

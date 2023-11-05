#ifndef GRID_H
#define GRID_H

// Define the grid properties and marker placement
#define GRID_WIDTH 10
#define GRID_HEIGHT 10

#define MARKER_COUNT 1
#define WALL_COUNT 4

struct Node
{
    int distance;
    int visited;
    int wall;
    int marker;
    int home;
    struct Node *previousNode;
    int robot;
    int x;
    int y;
};

extern struct Node grid[GRID_WIDTH][GRID_HEIGHT];

// Function prototypes for managing the grid and its elements
void initialiseGrid(int startX, int startY, int startDirection);

#endif /* GRID_H */

#ifndef GRID_H
#define GRID_H

// Grid dimensions and feature counts.
#define GRID_WIDTH 10
#define GRID_HEIGHT 10
#define WALL_COUNT 20
#define MARKER_COUNT 10

// Represents a single cell within the grid.
struct Node
{
    int distance;        // Distance from the robot's starting point.
    int visited;         // Visitation status of the node.
    int wall;            // Indicates if a wall is present.
    int marker;          // Indicates if a marker is present.
    int home;            // Indicates if this is the robot's home position.
    int previousNode[2]; // Coordinates of the previous node.
    int robot;           // Indicates if the robot is present.
    int x, y;            // X and Y coordinates of the node.
};

// Grid representation as a 2D array of Nodes.
extern struct Node grid[GRID_WIDTH][GRID_HEIGHT];

// Initializes the grid with starting position and direction of the robot.
void initialiseGrid(int startX, int startY, int startDirection);

#endif /* GRID_H */
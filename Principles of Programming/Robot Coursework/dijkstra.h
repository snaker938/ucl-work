#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "grid.h" // Include the grid structure and definitions

// Prototype for the dijkstra function which calculates the shortest path in a grid.
struct Node *dijkstra(struct Node grid[GRID_WIDTH][GRID_HEIGHT], int startX, int startY);

#endif // DIJKSTRA_H

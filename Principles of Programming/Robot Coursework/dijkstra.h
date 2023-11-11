// dijkstra.h
#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "grid.h" // Assuming grid.h contains the definition of struct Node and constants GRID_WIDTH and GRID_HEIGHT

struct Node *dijkstra(struct Node grid[GRID_WIDTH][GRID_HEIGHT], int startX, int startY);

#endif // DIJKSTRA_H

// dijkstra.h
#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "grid.h"

struct Node *dijkstra(struct Node grid[GRID_WIDTH][GRID_HEIGHT], int startX, int startY);

#endif // DIJKSTRA_H

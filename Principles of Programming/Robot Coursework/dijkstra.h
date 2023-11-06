#ifndef DIJKSTRA_H
#define DIJKSTRA_H

#include "grid.h"

int dijkstra(int startX, int startY, struct Node (*grid)[GRID_WIDTH][GRID_HEIGHT]);

#endif /* GRID_H */
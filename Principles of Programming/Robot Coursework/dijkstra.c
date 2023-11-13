
#include "grid.h"
#include "dijkstra.h"
#include "graphics.h"
#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // For INT_MAX

void getAllNodes(struct Node grid[GRID_WIDTH][GRID_HEIGHT], struct Node *allNodes[GRID_WIDTH * GRID_HEIGHT])
{
    int index = 0;
    for (int i = 0; i < GRID_WIDTH; i++)
    {
        for (int j = 0; j < GRID_HEIGHT; j++)
        {
            allNodes[index++] = &grid[i][j];
        }
    }
}

void sortNodesByDistance(struct Node **nodesToBeSorted, int n)
{
    struct Node *tempNode;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (nodesToBeSorted[j]->distance > nodesToBeSorted[j + 1]->distance)
            {
                tempNode = nodesToBeSorted[j];
                nodesToBeSorted[j] = nodesToBeSorted[j + 1];
                nodesToBeSorted[j + 1] = tempNode;
            }
        }
    }
}

void updateNeighbourDistances(struct Node *neighbours[], struct Node *currentNode, int neighbourCount)
{
    for (int i = 0; i < neighbourCount; i++)
    {
        if (neighbours[i]->distance > currentNode->distance + 1)
        {
            neighbours[i]->distance = currentNode->distance + 1;
            neighbours[i]->previousNode[0] = currentNode->x;
            neighbours[i]->previousNode[1] = currentNode->y;
        }
    }
}

void updateNeighboursOfNode(struct Node *currentNode, struct Node grid[GRID_WIDTH][GRID_HEIGHT])
{
    struct Node *neighbours[4] = {NULL};
    int neighbourCount = 0;

    int row = currentNode->x;
    int col = currentNode->y;

    if (row > 0 && !grid[row - 1][col].visited && !grid[row - 1][col].wall)
    {
        neighbours[neighbourCount++] = &grid[row - 1][col]; // Bottom neighbour
    }

    if (row < GRID_WIDTH - 1 && !grid[row + 1][col].visited && !grid[row + 1][col].wall)
    {
        neighbours[neighbourCount++] = &grid[row + 1][col]; // Top neighbour
    }

    if (col > 0 && !grid[row][col - 1].visited && !grid[row][col - 1].wall)
    {
        neighbours[neighbourCount++] = &grid[row][col - 1]; // Left neighbour
    }

    if (col < GRID_HEIGHT - 1 && !grid[row][col + 1].visited && !grid[row][col + 1].wall)
    {
        neighbours[neighbourCount++] = &grid[row][col + 1]; // Right neighbour
    }

    updateNeighbourDistances(neighbours, currentNode, neighbourCount);
}

struct Node *getShortestPath(struct Node grid[GRID_WIDTH][GRID_HEIGHT], struct Node endNode)
{
    struct Node *current = &endNode;
    int pathLength = 0;

    // Determine the length of the path
    while (current->previousNode[0] != -1)
    {
        pathLength++;
        int prevX = current->previousNode[0];
        int prevY = current->previousNode[1];
        current = &grid[prevX][prevY];
    }

    // Allocate an extra element for the terminator node
    struct Node *shortestPath = (struct Node *)malloc((pathLength + 2) * sizeof(struct Node)); // +2 for terminator node
    current = &endNode;

    // Fill the array backwards since we're traversing the path from end to start
    for (int i = pathLength; i >= 0; i--)
    {
        shortestPath[i] = *current;
        int prevX = current->previousNode[0];
        int prevY = current->previousNode[1];
        if (prevX == -1)
        {
            break;
        }
        current = &grid[prevX][prevY];
    }

    // Set the terminator node's values at the end
    shortestPath[pathLength + 1].x = -1;
    shortestPath[pathLength + 1].y = -1;
    shortestPath[pathLength + 1].previousNode[0] = -2; // Use -2 to differentiate from start node
    shortestPath[pathLength + 1].previousNode[1] = -2; // Use -2 to differentiate from start node

    return shortestPath;
}

struct Node *dijkstra(struct Node grid[GRID_WIDTH][GRID_HEIGHT], int startX, int startY)
{
    struct Node *allNodes[GRID_WIDTH * GRID_HEIGHT] = {NULL};
    getAllNodes(grid, allNodes);

    for (int i = 0; i < GRID_WIDTH * GRID_HEIGHT; i++)
    {
        allNodes[i]->distance = INT_MAX;
        allNodes[i]->previousNode[0] = -1;
        allNodes[i]->previousNode[1] = -1;
        allNodes[i]->visited = 0;
    }

    struct Node *startNode = &grid[startX][startY];
    startNode->distance = 0;

    int unvisitedCount = GRID_WIDTH * GRID_HEIGHT;

    struct Node *endNode = NULL;

    while (unvisitedCount > 0)
    {
        sortNodesByDistance(allNodes, unvisitedCount);

        struct Node *currentNode = allNodes[0];
        if (currentNode->distance == INT_MAX)
        {
            // No path exists if the closest unvisited node is at infinity distance
            return NULL;
        }

        currentNode->visited = 1;
        if (currentNode->marker)
        {
            // Marker found, this is the end node
            endNode = currentNode;
            break;
        }

        updateNeighboursOfNode(currentNode, grid);

        // Move the unvisited node array forward
        for (int i = 0; i < unvisitedCount - 1; i++)
        {
            allNodes[i] = allNodes[i + 1];
        }
        unvisitedCount--;
    }

    if (endNode == NULL)
    {
        // If the loop completes without finding the end marker, no path exists
        return NULL;
    }

    // If the end node is found, construct the shortest path
    return getShortestPath(grid, *endNode);
}

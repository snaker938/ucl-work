#include "grid.h"
#include "dijkstra.h"
#include "graphics.h"
#include <stdio.h>
#include <stdlib.h>

struct Node endNode;

void getAllNodes(struct Node grid[GRID_WIDTH][GRID_HEIGHT], struct Node *allNodes[GRID_WIDTH * GRID_HEIGHT])
{
    // For each node in the grid
    for (int i = 0; i < GRID_WIDTH; i++)
    {
        for (int j = 0; j < GRID_HEIGHT; j++)
        {
            // Add a pointer to the node in the allNodes array
            allNodes[i * GRID_WIDTH + j] = &grid[i][j];
        }
    }
}

// This function sorts all the nodes passed into it by their distance property
void sortNodesByDistance(struct Node *nodesToBeSorted)
{
    int n = GRID_WIDTH * GRID_HEIGHT;
    struct Node tempNode;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (&nodesToBeSorted[j] == NULL || &nodesToBeSorted[j + 1] == NULL)
            {
                continue; // Skip iteration if a NULL pointer is encountered
            }

            if (nodesToBeSorted[j].distance > nodesToBeSorted[j + 1].distance)
            {
                tempNode = nodesToBeSorted[j];
                nodesToBeSorted[j] = nodesToBeSorted[j + 1];
                nodesToBeSorted[j + 1] = tempNode;
            }
        }
    }
}

// Function to shift elements in an array to the left by one position
void shiftArray(struct Node *array, int length)
{
    for (int i = 0; i < length - 1; i++)
    {
        array[i] = array[i + 1];
    }
}

// This function updates the distances of the neighbours. If there are no nodes to update, then it does nothing
void updateNeighbourDistances(struct Node *neighbours[4], struct Node *currentNodePtr, int neighbourCount)
{
    for (int i = 0; i < neighbourCount; i++)
    {
        neighbours[i]->distance = currentNodePtr->distance + 1;
        neighbours[i]->previousNode = currentNodePtr;
    }
}

// Function to shift elements in an array to the right by one position
void shiftNeighbourElements(struct Node *neighbours[4])
{
    // Shift the elements to the right
    for (int i = 3; i > 0; i--)
    {
        neighbours[i] = neighbours[i - 1];
    }
}

// This function collects all the neighbours of the currentNode, then passes these nodes to a new function to update their distances
void updateNeighboursOfNode(struct Node *currentNodePtr, struct Node (*grid)[GRID_WIDTH][GRID_HEIGHT])
{
    // holds all the neighbours of the current node. The maximum neighbours is 4. The minimum could be zero. It does not matter if this is left empty at the end of this function
    struct Node *neighbours[4];

    int neighbourCount = 0;

    // define the row and column of the current node
    int row = (*currentNodePtr).x;
    int col = (*currentNodePtr).y;

    if (row > 0 && (*grid)[row - 1][col].distance > (*currentNodePtr).distance)
    {
        neighbourCount++;
        shiftNeighbourElements(neighbours);
        neighbours[0] = &(*grid)[row - 1][col];
    }

    if (row < GRID_WIDTH - 1 && (*grid)[row + 1][col].distance > (*currentNodePtr).distance)
    {
        neighbourCount++;
        shiftNeighbourElements(neighbours);
        neighbours[0] = &(*grid)[row + 1][col];
    }

    if (col > 0 && (*grid)[row][col - 1].distance > (*currentNodePtr).distance)
    {
        neighbourCount++;
        shiftNeighbourElements(neighbours);
        neighbours[0] = &(*grid)[row][col - 1];
    }

    if (
        col < GRID_WIDTH - 1 &&
        (*grid)[row][col + 1].distance > (*currentNodePtr).distance)
    {
        neighbourCount++;
        shiftNeighbourElements(neighbours);
        neighbours[0] = &(*grid)[row][col + 1];
    }

    // Update the distances of the neighbours of the currentNode
    updateNeighbourDistances(neighbours, currentNodePtr, neighbourCount);
}

// This function will only work once every node up to the end node has been updated. This function will infact never be called if the end node is not accessible.
struct Node *getShortestPath(struct Node visitedNodes[GRID_WIDTH * GRID_HEIGHT])
{
    // count how many nodes that do not have a distance of 9999 in the visitedNodes array
    int nodeCount = 0;

    for (int i = 0; i < GRID_WIDTH * GRID_HEIGHT; i++)
    {
        if (visitedNodes[i].distance != 9999)
        {
            nodeCount++;
        }
    }

    // Allocate memory for the shortestPath array
    struct Node *shortestPath = (struct Node *)malloc(nodeCount * sizeof(struct Node));

    // Define the currentNode and set it to the end node
    struct Node currentNode = endNode;

    // print the previous node of the currentNode
    printf("Previous node: (%d, %d)\n", currentNode.previousNode->x, currentNode.previousNode->y);

    // print the

    // This while loop will keep on backtracking through the previous node until the currentNode is null, which is when we have reached the start node - as the start node has no previous node.
    // while (currentNode.previousNode != NULL)
    // {
    //     // Add the currentNode to the shortestPath array
    //     shortestPath[nodeCount - 1] = currentNode;

    //     // Set the currentNode to the previous node
    //     currentNode = *(currentNode.previousNode);

    //     // Decrement nodeCount
    //     nodeCount--;
    // }

    // Return the shortestPath array
    // return shortestPath;
}

int dijkstra(int startX, int startY, struct Node (*grid)[GRID_WIDTH][GRID_HEIGHT])
{

    int visitedNodeIndex = 0;

    // This is a list of every node in the grid

    struct Node *allUnvisitedNodes[GRID_WIDTH * GRID_HEIGHT];

    getAllNodes((*grid), allUnvisitedNodes);

    // This is an empty list of visited nodes in the grid. The maximum number of nodes is GRID_WIDTH * GRID_HEIGHT
    struct Node visitedNodes[GRID_WIDTH * GRID_HEIGHT];

    // Set each visitedNode property to default initially
    for (int i = 0; i < GRID_WIDTH * GRID_HEIGHT; i++)
    {
        visitedNodes[i].previousNode = NULL;

        visitedNodes[i].wall = 0;
        visitedNodes[i].marker = 0;
        visitedNodes[i].visited = 0;
        visitedNodes[i].distance = 9999;
        visitedNodes[i].home = 0;
        visitedNodes[i].robot = 0;

        visitedNodes[i].x = -1;
        visitedNodes[i].y = -1;
    }

    // Define the variable currentNodePtr and set it to the address of start node. Retrieve the start node from the allUnvisitedNodes array
    struct Node *currentNodePtr = allUnvisitedNodes[((startX * 10) + startY)];

    (*currentNodePtr).distance = 0;

    // Add the start node to the list of visited nodes
    visitedNodes[visitedNodeIndex] = *currentNodePtr;

    // error checking
    int maxCheck = 0;

    while (maxCheck < GRID_HEIGHT * GRID_WIDTH)
    {
        maxCheck++;

        // Sorts the allUnvisitedNodes array by the distance property of each node
        sortNodesByDistance(*allUnvisitedNodes);

        // removes the first (closest) node from the allUnvisitedNodes array
        currentNodePtr = &(*allUnvisitedNodes[0]);

        allUnvisitedNodes[99] = NULL;

        // if the currentNode is a marker, then break out of the loop
        if ((*currentNodePtr).marker == 1)
        {
            printf("Marker found\n");
            // print x and y of current node
            printf("Marker: (%d, %d)\n", (*currentNodePtr).x, (*currentNodePtr).y);

            endNode = (*currentNodePtr);
            break;
        }

        // If the currentNode is a wall, then continue to the next iteration of the loop
        if ((*currentNodePtr).wall == 1)
        {
            continue;
        }

        // Update the distances of the neighbours of the currentNode
        updateNeighboursOfNode(currentNodePtr, grid);

        // If the current node is not a wall, add it to the list of visited nodes
        if ((*currentNodePtr).wall == 0)
        {
            visitedNodeIndex++;
            visitedNodes[visitedNodeIndex] = (*currentNodePtr);
        }

        int length = sizeof(allUnvisitedNodes) / sizeof(allUnvisitedNodes[0]);
        shiftArray(*allUnvisitedNodes, length);
    }

    // print the distance of index 2 of visited nodes

    // Once the end node has been reached...

    struct Node *shortestPath = getShortestPath(visitedNodes);

    // print out the shortest path
    // for (int i = 0; i < sizeof(shortestPath) / sizeof(shortestPath[0]); i++)
    // {
    //     printf("Shortest path: (%d, %d)\n", shortestPath[i].x, shortestPath[i].y);
    // }

    // sortNodesByDistance(visitedNodes);

    // Print the end node distance
    // printf("End node distance: %d\n", endNode.distance);

    // // If the endnode has not been reached (ie. it has a distance of 9999, which is the default value), set the shortest path to be the visited nodes, and return false
    // if (endNode.distance == 9999)
    // {
    //     return 0;
    // }

    // // If there is a shortest path to the end node: get it
    // // struct Node shortestPath[GRID_WIDTH * GRID_HEIGHT] = getShortestPath(endNode)

    // return 1;
}

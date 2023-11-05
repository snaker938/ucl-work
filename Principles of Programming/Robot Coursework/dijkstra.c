#include "grid.h"
#include "dijkstra.h"
#include "graphics.h"
#include <stdio.h>
#include <stdlib.h>

struct Node endNode;

// This function returns the shortest path to the end node
struct Node *getShortestPath(struct Node endNode)
{
    // Define the variable currentNode and set it to the end node
    struct Node currentNode = endNode;

    // Allocate memory for the shortestPath array
    struct Node *shortestPath = (struct Node *)malloc(GRID_WIDTH * GRID_HEIGHT * sizeof(struct Node));

    // Check if memory allocation was successful
    if (shortestPath == NULL)
    {
        printf("Memory allocation failed\n");
        return NULL; // Handle the error appropriately
    }

    // Define the variable i
    int i = 0;

    // While the currentNode is not the start node
    while (currentNode.distance != 0)
    {
        // Add the currentNode to the shortestPath array
        shortestPath[i] = currentNode;

        // Set the currentNode to the previous node
        currentNode = *(currentNode.previousNode);

        // Increment i
        i++;
    }

    // Return the shortestPath array
    return shortestPath;
}

// Function to shift elements in an array to the right by one position
void shiftNeighbourElements(struct Node neighbours[4])
{
    // Shift the elements to the right
    for (int i = 3; i > 0; i--)
    {
        neighbours[i] = neighbours[i - 1];
    }
}

// Function to get all nodes from 2D array and put them into a 1D array
void getAllNodes(struct Node grid[GRID_WIDTH][GRID_HEIGHT], struct Node allNodes[GRID_WIDTH * GRID_HEIGHT])
{
    // Define the variable i
    int i;

    // Define the variable j
    int j;

    // For each node in the grid
    for (i = 0; i < GRID_WIDTH; i++)
    {
        for (j = 0; j < GRID_HEIGHT; j++)
        {
            // Add the node to the allNodes array
            allNodes[i * GRID_WIDTH + j] = grid[i][j];
        }
    }
}

// This function sorts all the nodes passed into it by their distance property
void sortNodesByDistance(struct Node nodesToBeSorted[GRID_WIDTH * GRID_HEIGHT])
{
    // Define the variable n and set it to the length of the nodesToBeSorted array
    int n = GRID_WIDTH * GRID_HEIGHT;

    // Define the variable i
    int i;

    // Define the variable j
    int j;

    // Define the variable tempNode
    struct Node tempNode;

    // For each node in the nodesToBeSorted array
    for (i = 0; i < n; i++)
    {
        // For each node in the nodesToBeSorted array
        for (j = 0; j < n - 1; j++)
        {
            // If the distance of the current node is greater than the distance of the next node
            if (nodesToBeSorted[j].distance > nodesToBeSorted[j + 1].distance)
            {
                // Set the tempNode to the current node
                tempNode = nodesToBeSorted[j];

                // Set the current node to the next node
                nodesToBeSorted[j] = nodesToBeSorted[j + 1];

                // Set the next node to the tempNode
                nodesToBeSorted[j + 1] = tempNode;
            }
        }
    }
}

// Function to shift elements in an array to the left by one position
void shiftArray(struct Node array[], int length)
{
    for (int i = 0; i < length - 1; i++)
    {
        array[i] = array[i + 1];
    }
}

// This function updates the distances of the neighbours. If there are no nodes to update, then it does nothing
void updateNeighbourDistances(struct Node neighbours[4], struct Node currentNode)
{
    for (int i = 0; i < 4; i++)
    {
        neighbours[i].distance = currentNode.distance + 1;
        neighbours[1].previousNode = &currentNode;
    }
}

// This function collects all the neighbours of the currentNode, then passes these nodes to a new function to update their distances
void updateNeighboursOfNode(struct Node currentNode, struct Node grid[GRID_WIDTH][GRID_HEIGHT])
{
    // holds all the neighbours of the current node. The maximum neighbours is 4. The minimum could be zero. It does not matter if this is left empty at the end of this function
    struct Node neighbours[4];

    // define the row and column of the current node
    int row = currentNode.x;
    int col = currentNode.y;

    if (row > 0 && grid[row - 1][col].distance > currentNode.distance)
    {
        shiftNeighbourElements(neighbours);
        neighbours[0] = grid[row - 1][col];
    }

    if (row < GRID_WIDTH - 1 && grid[row + 1][col].distance > currentNode.distance)
    {
        shiftNeighbourElements(neighbours);
        neighbours[0] = grid[row + 1][col];
    }

    if (col > 0 && grid[row][col - 1].distance > currentNode.distance)
    {
        shiftNeighbourElements(neighbours);
        neighbours[0] = grid[row][col - 1];
    }

    if (
        col < GRID_WIDTH - 1 &&
        grid[row][col + 1].distance > currentNode.distance)
    {
        shiftNeighbourElements(neighbours);
        neighbours[0] = grid[row][col + 1];
    }

    // loop through the neighbours array, and print the (x,y) for each
    // for (int i = 0; i < 4; i++)
    // {
    //     printf("Neighbour %d: (%d, %d)\n", i, neighbours[i].x, neighbours[i].y);
    // }

    // Update the distances of the neighbours of the currentNode
    updateNeighbourDistances(neighbours, currentNode);
}

int dijkstra(int startX, int startY, struct Node grid[GRID_WIDTH][GRID_HEIGHT])
{

    int visitedNodeIndex = 0;

    // This is a list of every node in the grid

    struct Node allUnvisitedNodes[GRID_WIDTH * GRID_HEIGHT];

    getAllNodes(grid, allUnvisitedNodes);

    // This is an empty list of visited nodes in the grid. The maximum number of nodes is GRID_WIDTH * GRID_HEIGHT
    struct Node visitedNodes[GRID_WIDTH * GRID_HEIGHT];

    // Define the variable currentNode and set it to the start node
    struct Node currentNode = grid[startX][startY];

    // Set the distance of the start node to 0
    currentNode.distance = 0;

    // Add the start node to the list of visited nodes
    visitedNodes[visitedNodeIndex] = currentNode;

    // error checking
    // int error = 0;

    // sleep(1);

    /*
    while ((currentNode.x > GRID_WIDTH || currentNode.y > GRID_HEIGHT))
    {
        error++;
        if (error > 1)
        {
            printf("Error: infinite loop\n");
            break;
        }



        sleep(1);

        printf("Test 1");

        // Increment the visitedNodeIndex
        visitedNodeIndex++;

        // Sorts the allUnvisitedNodes array by the distance property of each node
        sortNodesByDistance(allUnvisitedNodes);

        // removes the first (closest) node from the allUnvisitedNodes array
        currentNode = allUnvisitedNodes[0];

        int length = sizeof(allUnvisitedNodes) / sizeof(allUnvisitedNodes[0]);
        shiftArray(allUnvisitedNodes, length);

        printf("Test 2");

        // if the currentNode is a marker, then break out of the loop
        if (currentNode.marker == 1)
        {
            endNode = currentNode;
            break;
        }

        // If the currentNode is a wall, then continue to the next iteration of the loop
        if (currentNode.wall == 1)
        {
            continue;
        }

        printf("Test 3");

        // Update the distances of the neighbours of the currentNode
        updateNeighboursOfNode(currentNode, grid);

        // If the current node is not a wall, add it to the list of visited nodes
        if (currentNode.wall == 0)
        {
            visitedNodes[visitedNodeIndex] = currentNode;
        }


    }
    */

    // Once the end node has been reached...

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

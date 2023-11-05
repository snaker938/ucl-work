#include "grid.h"
#include <stdio.h>
#include "graphics.h"
#include "utils.h"
#include "dijkstra.h"

struct Node grid[GRID_WIDTH][GRID_HEIGHT];

int gridTopLeftCoords[GRID_WIDTH][GRID_HEIGHT][2];
int SQUARE_SIZE;

// Function to display the marker
void displayMarker(int x, int y)
{
    setColour(gray);
    fillRect(gridTopLeftCoords[x][y][0], gridTopLeftCoords[x][y][1], SQUARE_SIZE, SQUARE_SIZE);
}

// Function to display the wall
void displayWall(int x, int y)
{
    setColour(black);
    fillRect(gridTopLeftCoords[x][y][0], gridTopLeftCoords[x][y][1], SQUARE_SIZE, SQUARE_SIZE);
}

// Function to display the home square
void displayHome(int x, int y)
{
    setColour(blue);
    fillRect(gridTopLeftCoords[x][y][0], gridTopLeftCoords[x][y][1], SQUARE_SIZE, SQUARE_SIZE);
}

// Function to display the robot which is a triangle pointing in the direction of the variable "direction"
void displayRobot(int x, int y, int direction)
{
    // Set the colour to red to represent the robot
    setColour(red);

    // Define the size of the robot triangle
    int robotSize = SQUARE_SIZE / 2;

    // Define the points of the triangle based on the robot's position and direction
    int topLeftX = gridTopLeftCoords[x][y][0];
    int topLeftY = gridTopLeftCoords[x][y][1];
    int xPoints[3];
    int yPoints[3];

    // Calculate the coordinates for the triangle based on the direction
    switch (direction)
    {
    case 0: // North
        xPoints[0] = topLeftX + SQUARE_SIZE / 2;
        yPoints[0] = topLeftY;
        xPoints[1] = topLeftX;
        yPoints[1] = topLeftY + SQUARE_SIZE;
        xPoints[2] = topLeftX + SQUARE_SIZE;
        yPoints[2] = topLeftY + SQUARE_SIZE;
        break;
    case 1: // West
        xPoints[0] = topLeftX;
        yPoints[0] = topLeftY + SQUARE_SIZE / 2;
        xPoints[1] = topLeftX + SQUARE_SIZE;
        yPoints[1] = topLeftY;
        xPoints[2] = topLeftX + SQUARE_SIZE;
        yPoints[2] = topLeftY + SQUARE_SIZE;
        break;
    case 2: // South
        xPoints[0] = topLeftX + SQUARE_SIZE / 2;
        yPoints[0] = topLeftY + SQUARE_SIZE;
        xPoints[1] = topLeftX;
        yPoints[1] = topLeftY;
        xPoints[2] = topLeftX + SQUARE_SIZE;
        yPoints[2] = topLeftY;
        break;
    case 3: // East
        xPoints[0] = topLeftX + SQUARE_SIZE;
        yPoints[0] = topLeftY + SQUARE_SIZE / 2;
        xPoints[1] = topLeftX;
        yPoints[1] = topLeftY;
        xPoints[2] = topLeftX;
        yPoints[2] = topLeftY + SQUARE_SIZE;
        break;
    }

    // Call the fillPolygon function to draw the triangle representing the robot
    fillPolygon(3, xPoints, yPoints);
}

// Function to display the grid
// Function to display the empty grid
void displayGrid(int direction, int startX, int startY)
{
    // Implement the code to display the grid
    int gridSize, xOffset, yOffset;
    int minOffset = 10;

    if (WIN_WIDTH - 2 * minOffset < WIN_HEIGHT - 2 * minOffset)
    {
        gridSize = WIN_WIDTH - 2 * minOffset;
        xOffset = minOffset;
        yOffset = (WIN_HEIGHT - gridSize) / 2;
    }
    else
    {
        gridSize = WIN_HEIGHT - 2 * minOffset;
        xOffset = (WIN_WIDTH - gridSize) / 2;
        yOffset = minOffset;
    }

    // Draw the grid with the largest possible square within the window
    int i, j;
    for (i = 0; i <= GRID_HEIGHT; i++)
    {
        for (j = 0; j <= GRID_WIDTH; j++)
        {
            // draw the vertical lines
            drawLine(xOffset + j * (gridSize / GRID_WIDTH), yOffset, xOffset + j * (gridSize / GRID_WIDTH), yOffset + gridSize);

            // draw the horizontal lines
            drawLine(xOffset, yOffset + i * (gridSize / GRID_HEIGHT), xOffset + gridSize, yOffset + i * (gridSize / GRID_HEIGHT));

            // store the top left coordinates of each square
            gridTopLeftCoords[i][j][0] = xOffset + j * (gridSize / GRID_WIDTH);
            gridTopLeftCoords[i][j][1] = yOffset + i * (gridSize / GRID_HEIGHT);
        }
    }

    SQUARE_SIZE = gridSize / GRID_WIDTH;

    // Call the functions to display the elements based on the last non-empty element in the 1D array
    for (i = 0; i < GRID_HEIGHT; i++)
    {
        for (j = 0; j < GRID_WIDTH; j++)
        {
            if (grid[i][j].marker == 1)
            {
                displayMarker(i, j);
            }
            if (grid[i][j].wall == 1)
            {
                displayWall(i, j);
            }
            if (grid[i][j].home == 1)
            {
                displayHome(i, j);
            }
            if (grid[i][j].robot == 1)
            {
                displayRobot(i, j, direction);
            }
        }
    }
    dijkstra(startX, startY, grid);
}

void initialiseGrid(int startX, int startY, int startDirection)
{
    for (int i = 0; i < GRID_WIDTH; i++)
    {
        for (int j = 0; j < GRID_HEIGHT; j++)
        {

            grid[i][j].previousNode = NULL;

            grid[i][j].wall = 0;
            grid[i][j].marker = 0;
            grid[i][j].visited = 0;
            grid[i][j].distance = 9999;
            grid[i][j].home = 0;
            grid[i][j].robot = 0;

            grid[i][j].x = i;
            grid[i][j].y = j;

            // Set the walls
            if (i == 2 && j == 3)
            {
                grid[i][j].wall = 1;
            }

            // Set the markers
            if (i == 4 && j == 5)
            {
                grid[i][j].marker = 1;
            }

            if (i == startX && j == startY)
            {
                grid[i][j].home = 1;
                grid[i][j].robot = 1;
            }
        }
    }

    // Display the grid
    displayGrid(startDirection, startX, startY);
}
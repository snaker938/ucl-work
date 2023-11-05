// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <math.h>
// #include <time.h>
// #include "graphics.h"

// // Set the window size here
// int windowWidth = 1400;
// int windowHeight = 600;

// void drawSpiral(int centerX, int centerY, int numTurns, int numSegments, float angle, float maxRadius, int offset)
// {
//     float angleIncrement = 2 * 3.141592653589793238462643383279502884197 / numSegments;
//     float radiusStep = maxRadius / (numSegments * numTurns);

//     for (int spiralNumber = 0; spiralNumber < numSegments * numTurns; spiralNumber++)
//     {
//         int red = rand() % 256;
//         int green = rand() % 256;
//         int blue = rand() % 256;

//         setRGBColour(red, green, blue);

//         float currentRadius = spiralNumber * radiusStep;
//         float startAngle = angle + spiralNumber * angleIncrement;
//         float endAngle = startAngle + angleIncrement;

//         // if the value of spiralNumber is smaller than the offset, then draw the arc at the normal position of centerX and centerY. Else, draw the arc at the position windowWidth /2 and windowHeight /2

//         if (spiralNumber <= offset)
//         {
//             centerX = windowWidth / 2;
//             centerY = windowHeight / 2;
//         }

//         drawArc(centerX, centerY, (int)currentRadius, (int)currentRadius, 0, 360);
//         // sleep(300);
//     }
// }

// void drawSpinningSpiralAnimation()
// {
//     int X = 0;
//     int Y = 0;
//     float angle = 0.0;
//     int numTurns = 6;
//     int numSegments = 20;

//     for (int i = 0; i < 100; i++)
//     {
//         clear();
//         drawSpiral(X, Y, numTurns, numSegments, angle, 1000.0, -1);
//         angle += 0.1; // Adjust the angle increment for speed of rotation
//         sleep(100);   // Adjust the sleep duration for speed of animation
//     }

//     //  Move each circle to the centre, one at a time, starting with the innermost circle. There are numSegments * numTurns circles in total.

//     // For each circle
//     for (int i = 0; i < numSegments * numTurns; i++)
//     {
//         // Clear the screen
//         clear();
//         // Draw the all the circles up to i at the centre. The rest of the circles will be drawn at their normal position
//         drawSpiral(X, Y, numTurns, numSegments, angle, 250, i);

//         angle += 0.1; // Adjust the angle increment for speed of rotation
//         sleep(500);
//     }
// }

// int main()
// {
//     srand(time(NULL)); // Initialize random seed

//     setWindowSize(windowWidth, windowHeight);
//     drawSpinningSpiralAnimation();
//     return 0;
// }

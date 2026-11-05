#include <stdio.h>

int main()
{
    float x1 = 2, y1 = -2;
    float x2 = 3, y2 = 7;
    float py = 11.0 / 24.0;
    float m = 59, n = 205, x;

    // Calculate the x-coordinate using the section formula.
    x = (m * x2 + n * x1) / (m + n);

    printf("Ratio = %.0f : %.0f\n", m, n);

    // Print the coordinates of the dividing point.
    printf("Point = (%.4f, %.4f)\n", x, py);

    return 0;
}

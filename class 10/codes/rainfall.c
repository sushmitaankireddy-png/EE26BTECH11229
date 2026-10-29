#include <stdio.h>

int main()
{
    float roofArea = 22 * 20;
    float radius = 1, height = 3.5;
    float pi = 22.0 / 7.0;
    float tankVolume, rainfall;

    // Calculate the volume of water stored in the tank.
    tankVolume = pi * radius * radius * height;

    // Rainfall depth = volume collected / roof area.
    rainfall = tankVolume / roofArea;

    // Convert the rainfall depth from metres to centimetres.
    rainfall = rainfall * 100;

    printf("Rainfall = %.2f cm\n", rainfall);

    return 0;
}

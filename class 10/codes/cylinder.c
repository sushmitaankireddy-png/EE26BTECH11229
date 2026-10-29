#include <stdio.h>

int main()
{
    float l, b, h;
    float R, r, length;
    float pi = 3.14159;

    // Read the dimensions of the original cuboid.
    printf("Enter cuboid length, breadth and height: ");
    scanf("%f %f %f", &l, &b, &h);

    // Read the outer and inner radii of the cylinder.
    printf("Enter outer and inner radii: ");
    scanf("%f %f", &R, &r);

    // Equate the cuboid and hollow-cylinder volumes.
    length = (l * b * h) / (pi * (R * R - r * r));

    printf("Length of hollow cylinder = %.2f\n", length);

    return 0;
}

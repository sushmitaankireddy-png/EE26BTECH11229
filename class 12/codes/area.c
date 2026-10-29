#include <stdio.h>

int main() {
    double x = 8, y = 6;
    double dx = -5, dy = 4;
    double rate;

    // Differentiate A = x*y with respect to time
    rate = x * dy + y * dx;

    // Display the rate of change of area
    printf("Rate of change of area = %.2f cm^2/min\n", rate);

    return 0;
}


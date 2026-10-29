#include <stdio.h>
#include <math.h>

// Write the given equation in the form f(x) = 0
double f(double x) {
    return atan((x-3)/(x-4))
         + atan((x+3)/(x+4)) - M_PI/4;
}

double bisection(double a, double b) {
    double mid;
    int i;

    // Repeatedly halve the interval containing the root
    for (i = 0; i < 100; i++) {
        mid = (a + b) / 2;

        if (f(a) * f(mid) < 0)
            b = mid;
        else
            a = mid;
    }

    return (a + b) / 2;
}

int main() {
    double x1, x2;

    // Choose intervals that bracket the roots
    x1 = bisection(-3.0, -2.8);
    x2 = bisection(2.8, 3.0);

    printf("First root = %.4f\n", x1);
    printf("Second root = %.4f\n", x2);

    return 0;
}


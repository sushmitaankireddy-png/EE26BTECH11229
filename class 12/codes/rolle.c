
#include <stdio.h>
#include <math.h>

int main() {
    double c = -1.5, next;
    int i;

    // Solve f'(c) = 3c^2 - 3 = 0 using Newton-Raphson
    for (i = 0; i < 20; i++) {
        next = c - (3*c*c - 3) / (6*c);

        // Stop when the successive values are sufficiently close
        if (fabs(next - c) < 0.000001)
            break;

        c = next;
    }

    printf("Value of c = %.4f\n", next);

    return 0;
}


#include <stdio.h>

int main()
{
    float p, r;

    // Let the roots be r and 6r.
    // Their sum is 14/p and product is 8/p.
    p = 3;
    r = 2.0 / p;

    printf("p = %.0f\n", p);

    // Display both roots of the equation.
    printf("Roots are %.2f and %.2f\n", r, 6 * r);

    return 0;
}

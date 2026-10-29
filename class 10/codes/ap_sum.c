#include <stdio.h>

int main()
{
    int n, sum;

    // Try possible numbers of terms.
    for (n = 1; n <= 100; n++)
    {
        // Calculate the sum using the A.P. formula.
        sum = n * (2 * 9 + (n - 1) * 8) / 2;

        // Check whether the sum equals 636.
        if (sum == 636)
        {
            printf("Number of terms = %d\n", n);
            break;
        }
    }

    return 0;
}

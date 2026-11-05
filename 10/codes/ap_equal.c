#include <stdio.h>

int main()
{
    int n, term1, term2;

    // Check successive terms of both A.P.s.
    for (n = 1; n <= 100; n++)
    {
        term1 = 63 + (n - 1) * 2;
        term2 = 3 + (n - 1) * 7;

        // Stop when the terms become equal.
        if (term1 == term2)
        {
            printf("n = %d\n", n);
            break;
        }
    }

    return 0;
}

#include <stdio.h>

int main()
{
    int a, b;
    int evenSum = 0, evenProduct = 0;

    // Generate all 36 possible outcomes.
    for (a = 1; a <= 6; a++)
    {
        for (b = 1; b <= 6; b++)
        {
            // Count outcomes with an even sum.
            if ((a + b) % 2 == 0)
                evenSum++;

            // Count outcomes with an even product.
            if ((a * b) % 2 == 0)
                evenProduct++;
        }
    }

    printf("Probability of even sum = %d/36\n", evenSum);
    printf("Probability of even product = %d/36\n", evenProduct);

    return 0;
}

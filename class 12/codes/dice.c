#include <stdio.h>

int main() {
    int i, even = 0, red = 0, both = 0;
    double pA, pB, pAB;

    // Count the outcomes belonging to each event
    for (i = 1; i <= 6; i++) {
        if (i % 2 == 0)
            even++;
        if (i <= 3)
            red++;
        if (i % 2 == 0 && i <= 3)
            both++;
    }

    // Calculate the probabilities
    pA = even / 6.0;
    pB = red / 6.0;
    pAB = both / 6.0;

    printf("P(A) = %.4f\n", pA);
    printf("P(B) = %.4f\n", pB);
    printf("P(A intersection B) = %.4f\n", pAB);

    // Check the condition for independent events
    printf("P(A) * P(B) = %.4f\n", pA * pB);

    if (pAB == pA * pB)
        printf("Events are independent.\n");
    else
        printf("Events are not independent.\n");

    return 0;
}


#include <stdio.h>

int main()
{
    int b;
    float timeA, totalWork;

    // Assume B takes b days, so A takes b - 6 days.
    for (b = 7; b <= 100; b++)
    {
        timeA = b - 6;

        // Add their individual daily work rates.
        totalWork = 1.0 / timeA + 1.0 / b;

        // Together, they must complete 1/4 of the work per day.
        if (totalWork == 0.25)
        {
            printf("B takes %d days\n", b);
            break;
        }
    }

    return 0;
}

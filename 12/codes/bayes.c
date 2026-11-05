#include <stdio.h>

int main() {
    double regular = 0.30, irregular = 0.70;
    double gradeR = 0.70, gradeI = 0.10;
    double totalGrade, probability;

    // Find the total probability of receiving an A grade
    totalGrade = regular * gradeR + irregular * gradeI;

    // Apply Bayes' theorem to find the probability of regular attendance
    probability = regular * gradeR / totalGrade;

    printf("P(regular | A grade) = %.2f\n", probability);

    return 0;
}


#include <stdio.h>
#include <math.h>

double f(double x){
    return x * sin(x) / (1.0 + sin(x));
}

int main()
{
    double pi = acos(-1.0);
    double a = 0.0, b = pi;
    double exact = pi * (pi - 2.0) / 2.0;
    int N[] = {10, 100, 1000, 10000};

    for (int j = 0; j < 4; j++) {
        int n_steps = N[j];
        double h = (b - a) / n_steps;
        double I = 0.0;                 /* I_0 = 0 */

        for (int n = 0; n < n_steps; n++) {
            double xn = a + n * h;
            double xn1 = a + (n + 1) * h;
            I = I + (h / 2.0) * (f(xn) + f(xn1));   /* I_{n+1} */
        }

        printf("N = %5d, I_N = %.6f, exact = %.6f, error = %.2e\n",
               n_steps, I, exact, fabs(I - exact));
    }

    return 0;
}

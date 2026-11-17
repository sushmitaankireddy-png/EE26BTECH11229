#include <stdio.h>
#include <math.h>

/* f(x) = x^2 + 4x + 4 */
double f(double x){
	return x*x + 4*x + 4;
}

/* f'(x) = 2x + 4 */
double df(double x){
	return 2*x + 4;
}

int main()
{
	double x = 0.0;        /* initial guess x_0 */
	double tol = 1e-10;    /* stop when |f(x)| is below this */
	int n = 0;             /* iteration counter */

	printf("n = %2d, x = %.10f\n", n, x);

	/* Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n) */
	while (fabs(f(x)) > tol && n < 100 && df(x) != 0) {
		x = x - f(x)/df(x);
		n++;
		printf("n = %2d, x = %.10f\n", n, x);
	}

	/* the iterates tend to the repeated root x = -2 */
	printf("Root: x = %.5f after %d iterations\n", x, n);
	return 0;
}

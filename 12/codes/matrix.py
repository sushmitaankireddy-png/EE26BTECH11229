import numpy as np

# Given matrices in the question
M = np.array([[2, -1], [1, 0], [-3, 4]], dtype=float)
N = np.array([[-1, -8], [1, -2], [9, 22]], dtype=float)

# Find the least-squares solution
A, residuals, rank, s = np.linalg.lstsq(M, N, rcond=None)

print("Matrix A =")
print(np.round(A, 2))

# Check whether the equation is satisfied
print("Residual =", np.round(M @ A - N, 2))


import numpy as np

a = 2

A = np.array([
    [a**2 + 2*a, 2*a + 1, 1],
    [2*a + 1, a + 2, 1],
    [3, 3, 1]
], dtype=float)

det = np.linalg.det(A)

print("Matrix A:")
print(A)

print("Determinant using NumPy =", round(det))
print("Expected value =", (a - 1)**3)

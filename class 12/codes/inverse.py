import numpy as np

# Coefficient matrix and constants
A = np.array([[2, -3, 5],
              [3, 2, -4],
              [1, 1, -2]], dtype=float)

B = np.array([11, -5, -3], dtype=float)

# Find the inverse and solve the equations
A_inv = np.linalg.inv(A)
solution = A_inv @ B

print("Inverse matrix =")
print(np.round(A_inv, 2))

print("Solution [x, y, z] =")
print(np.round(solution, 2))


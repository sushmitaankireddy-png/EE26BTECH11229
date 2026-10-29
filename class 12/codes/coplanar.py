import numpy as np

# Points given in the question
A = np.array([3, 2, 1])
C = np.array([4, 2, -2])
D = np.array([6, 5, -1])

# Coplanarity requires the scalar triple product to be zero
def determinant(x):
    B = np.array([4, x, 5])
    return np.linalg.det(np.array([B-A, C-A, D-A]))

# Since only B's y-coordinate contains x, det is linear in x.
# So, f(x) = f(0) + x[f(1) - f(0)].
# To find f(x) = 0, solve this linear equation for x.
d0 = determinant(0)
d1 = determinant(1)
x = -d0 / (d1 - d0)

print("Value of x =", round(x, 2))
print("Verification =", round(determinant(x), 6))


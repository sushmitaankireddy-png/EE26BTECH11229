import numpy as np

# First plane
A1 = np.array([2, -1, 2], dtype=float)
D1 = 5

# Second plane
A2 = np.array([5, -2.5, 5], dtype=float)
D2 = 20

# Normalize the second plane
A2 = A2 / 2.5
D2 = D2 / 2.5

# Find distance if planes are parallel
if np.allclose(A1, A2):
    distance = abs(D2 - D1) / np.linalg.norm(A1)
    print("Distance =", distance)
else:
    print("Planes are not parallel")

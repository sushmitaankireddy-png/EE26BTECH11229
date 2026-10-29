import numpy as np

# Position vectors of A, B and C
A = np.array([2, -1, 1])
B = np.array([1, -3, -5])
C = np.array([3, -4, -4])

# Check the angle at C using the dot product
CA = A - C
CB = B - C
print("Dot product =", np.dot(CA, CB))

# Calculate the triangle's area
area = np.linalg.norm(np.cross(CA, CB)) / 2
print("Area =", area)


import numpy as np

# Points defining the line
P = np.array([3, -4, -5])
Q = np.array([2, -3, 1])
direction = Q - P

# Points defining the plane
A = np.array([1, 2, 3])
B = np.array([4, 2, -3])
C = np.array([0, 4, 3])

# Find the normal vector of the plane
normal = np.cross(B - A, C - A)

# Calculate the line parameter t
t = np.dot(normal, A - P) / np.dot(normal, direction)
point = P + t * direction

print("Intersection point =", np.round(point, 2))


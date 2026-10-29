import numpy as np

# Constraints: 6x + 10y >= 60, 4x + 4y >= 32
A = np.array([[6, 10], [4, 4]])
b = np.array([60, 32])

# Find the intersection of the constraint boundaries
days = np.linalg.solve(A, b)
cost = 300 * days[0] + 400 * days[1]

# Compare with the feasible axis-boundary points
candidates = np.array([[5, 3], [30, 0], [0, 8]])
costs = 300 * candidates[:, 0] + 400 * candidates[:, 1]
best = np.argmin(costs)

print("Intersection =", days)
print("Minimum cost =", costs[best])
print("Working days =", candidates[best])


import numpy as np
import matplotlib.pyplot as plt

# Plane through A, B, C and line through D, E
A = np.array([1, 2, 3])
B = np.array([4, 2, -3])
C = np.array([0, 4, 3])
D = np.array([3, -4, -5])
E = np.array([2, -3, 1])

# Solve A + l(B - A) + m(C - A) = D + k(E - D)
M = np.column_stack((B - A, C - A, D - E))
l, m, k = np.linalg.solve(M, D - A)
P = D + k * (E - D)
print("l, m, k =", l, m, k)
print("Intersection point =", P)

# Plane through A, B, C
n = np.cross(B - A, C - A)
gx, gy = np.meshgrid(np.linspace(-1, 5, 10), np.linspace(-5, 5, 10))
gz = A[2] - (n[0] * (gx - A[0]) + n[1] * (gy - A[1])) / n[2]

# Line
t = np.linspace(-0.5, 2.5, 50)
L = D[:, None] + (E - D)[:, None] * t

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(gx, gy, gz, color="tab:blue", alpha=0.3)
ax.plot(L[0], L[1], L[2], color="tab:green")
ax.scatter(*P, color="red")
ax.text(P[0], P[1], P[2], "P")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Line crossing the plane")

plt.savefig("figs/lineplane.png")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Points, with x = 5
x = 5
A = np.array([3, 2, 1])
B = np.array([4, x, 5])
C = np.array([4, 2, -2])
D = np.array([6, 5, -1])

# Direction matrix and its rank
M = np.column_stack((B - A, C - A, D - A))
print("M =")
print(M)
print("rank(M) =", np.linalg.matrix_rank(M))

# Plane through A, C, D
n = np.cross(C - A, D - A)
print("n =", n, ", n.(B - A) =", n @ (B - A))

gx, gy = np.meshgrid(np.linspace(2, 7, 10), np.linspace(1, 6, 10))
gz = A[2] - (n[0] * (gx - A[0]) + n[1] * (gy - A[1])) / n[2]

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(gx, gy, gz, color="tab:blue", alpha=0.3)

for V, name in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
    ax.scatter(*V, color="black")
    ax.text(V[0], V[1], V[2], name)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Coplanar points A, B, C, D")

plt.savefig("figs/coplanar.png")
plt.show()

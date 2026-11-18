import numpy as np
import matplotlib.pyplot as plt

# Vertices
A = np.array([2, -1, 1])
B = np.array([1, -3, -5])
C = np.array([3, -4, -4])

# Sides
AB = B - A
BC = C - B
CA = A - C

# Check for the right angle using dot products
print("AB.BC =", AB @ BC)
print("BC.CA =", BC @ CA)
print("CA.AB =", CA @ AB)
print("|BC|^2 + |CA|^2 =", BC @ BC + CA @ CA, ", |AB|^2 =", AB @ AB)

# Area from the cross product
area = 0.5 * np.linalg.norm(np.cross(BC, CA))
print("Area =", area, ", sqrt(210)/2 =", np.sqrt(210) / 2)

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

P = np.array([A, B, C, A])
ax.plot(P[:, 0], P[:, 1], P[:, 2], color="tab:blue")

for V, name in [(A, "A"), (B, "B"), (C, "C")]:
    ax.scatter(*V, color="black")
    ax.text(V[0], V[1], V[2], name)

# Right angle marker at C
u = (B - C) / np.linalg.norm(B - C)
v = (A - C) / np.linalg.norm(A - C)
s = 0.4
M = np.array([C + s*u, C + s*u + s*v, C + s*v])
ax.plot(M[:, 0], M[:, 1], M[:, 2], color="red")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Right-angled triangle ABC (right angle at C)")

plt.savefig("figs/triangle.png")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Planes: 2x - y + 2z = 5 and 5x - 2.5y + 5z = 20
x, y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))
z1 = (5 - 2*x + y) / 2
z2 = (20 - 5*x + 2.5*y) / 5

# Common normal and the points where it meets each plane
n = np.array([2, -1, 2])
p1 = 5 / np.dot(n, n) * n    # point on the first plane
p2 = 8 / np.dot(n, n) * n    # point on the second plane (2x - y + 2z = 8)
print("distance =", np.linalg.norm(p2 - p1))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(x, y, z1, color="tab:blue", alpha=0.5)
ax.plot_surface(x, y, z2, color="tab:orange", alpha=0.5)
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color="tab:green", linewidth=2)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("distance between parallel planes")

ax.legend(handles=[
    Line2D([0], [0], color="tab:blue", label="2x - y + 2z = 5"),
    Line2D([0], [0], color="tab:orange", label="5x - 2.5y + 5z = 20"),
    Line2D([0], [0], color="tab:green", label="d = 1"),
], loc="upper left", fontsize=8)

plt.savefig("figs/distance.png", dpi=150, bbox_inches="tight")
plt.show()

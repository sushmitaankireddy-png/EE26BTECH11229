import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Objective Z = c^T [x, y] and corner points of the feasible region (2xN matrix)
c = np.array([34.0, 45.0])
corners = np.block([
    np.array([0.0, 0.0]).reshape(-1, 1),
    np.array([35.0, 0.0]).reshape(-1, 1),
    np.array([0.0, 70 / 3]).reshape(-1, 1)
])

# Evaluate Z at every corner and pick the maximum
Z = c @ corners
best = np.argmax(Z)
print("Z at corners O, A, B =", np.round(Z, 4))
print(f"Max Z = {Z[best]:.4f} at (x, y) = ({corners[0, best]:.4f}, {corners[1, best]:.4f})")

# Initialize single figure plot
fig, ax = plt.subplots(figsize=(8, 6))

# Shade the feasible region
ax.fill(corners[0, :], corners[1, :], color="orange", alpha=0.35, label="Feasible region")

# Constraint line 2x + 3y = 70 using line_gen
A_c = np.array([35.0, 0.0]).reshape(-1, 1)
B_c = np.array([0.0, 70 / 3]).reshape(-1, 1)
con = line_gen(A_c, B_c)
ax.plot(con[0, :], con[1, :], color="blue", lw=2.5, label=r"$2x+3y=70$")

# Iso-profit line through the optimum: 34x + 45y = 1190
A_z = np.array([0.0, Z[best] / 45]).reshape(-1, 1)
B_z = np.array([Z[best] / 34, 0.0]).reshape(-1, 1)
iso = line_gen(A_z, B_z)
ax.plot(iso[0, :], iso[1, :], color="crimson", linestyle="--", lw=2,
        label=rf"$Z=34x+45y={Z[best]:.0f}$")

# Generate coordinate axes using line_gen
A_x = np.array([0.0, 0.0]).reshape(-1, 1)
B_x = np.array([45.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_x, B_x)
ax.plot(x_axis[0, :], x_axis[1, :], color="black", lw=1)

A_y = np.array([0.0, 0.0]).reshape(-1, 1)
B_y = np.array([0.0, 45.0]).reshape(-1, 1)
y_axis = line_gen(A_y, B_y)
ax.plot(y_axis[0, :], y_axis[1, :], color="black", lw=1)

# Plot and label the corner points
ax.plot(corners[0, :], corners[1, :], "o", color="darkred", markersize=6, zorder=5)
label_pts(corners, ["O (0, 0)", "A (35, 0) [max]", "B (0, 70/3)"])

# Plot formatting
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_xlim(-2, 45)
ax.set_ylim(-2, 45)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper right")

plt.tight_layout()
#If using termux
plt.savefig("figs/LPP.png")
#subprocess.run(shlex.split("termux-open figs/LPP.png"))
#else
plt.show()

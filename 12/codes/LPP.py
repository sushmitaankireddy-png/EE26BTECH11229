import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

# LPP: maximise Z = 34x + 45y
c = np.array([34, 45])
M = np.array([[1, 1], [2, 3]])
b = np.array([300, 70])

# Solve using cvxpy
x = cp.Variable(2)
prob = cp.Problem(cp.Maximize(c @ x), [M @ x <= b, x >= 0])
prob.solve()
xo, yo = x.value
zo = prob.value
print("x, y =", xo, yo)
print("Maximum Z =", zo)

fig, ax = plt.subplots(figsize=(8, 6))

# Constraint lines
xs = np.linspace(0, 40, 400)
ax.plot(xs, (70 - 2 * xs) / 3, color="tab:blue", label=r"$2x+3y=70$")
ax.plot(xs, 300 - xs, color="tab:green", label=r"$x+y=300$ (outside this window, redundant)")

# Feasible region: triangle with corner points (0,0), (35,0), (0,70/3)
corners = np.array([[0, 0], [35, 0], [0, 70 / 3]])
ax.fill(corners[:, 0], corners[:, 1], color="lightblue", alpha=0.5, label="Feasible region")

# Corner points with the value of Z
for px, py in corners:
    z = c @ np.array([px, py])
    ax.plot(px, py, "ko")
    ax.annotate(f"({px:.0f}, {py:.2f})\nZ = {z:.0f}", (px, py),
                textcoords="offset points", xytext=(8, 8), fontsize=9)

# Optimum and the line Z = 1190 passing through it
ax.plot(xo, yo, "ro", markersize=9, label=f"Maximum: Z = {zo:.0f} at ({xo:.0f}, {yo:.0f})")
ax.plot(xs, (zo - 34 * xs) / 45, "r--", linewidth=1, label=r"$34x+45y=1190$")

ax.set_xlim(-2, 40)
ax.set_ylim(-2, 40)
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"Maximise $Z=34x+45y$ subject to $x+y\leq 300,\ 2x+3y\leq 70,\ x,y\geq 0$")
ax.legend(loc="upper right", fontsize=8)
ax.grid(True)
plt.savefig("figs/LPP.png", dpi=200, bbox_inches="tight")
plt.show()

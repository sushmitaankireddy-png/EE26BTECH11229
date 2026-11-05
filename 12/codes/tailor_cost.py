import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

# LPP: minimise Z = 300x + 400y
c = np.array([300, 400])
M = np.array([[6, 10], [4, 4]])
b = np.array([60, 32])

# Solve using cvxpy
x = cp.Variable(2)
prob = cp.Problem(cp.Minimize(c @ x), [M @ x >= b, x >= 0])
prob.solve()
xo, yo = x.value
zo = prob.value
print("x, y =", xo, yo)
print("Minimum Z =", zo)

fig, ax = plt.subplots(figsize=(8, 6))

# Constraint lines
xs = np.linspace(0, 14, 400)
ax.plot(xs, (60 - 6 * xs) / 10, color="tab:blue", label=r"$6x+10y=60$ (shirts)")
ax.plot(xs, (32 - 4 * xs) / 4, color="tab:green", label=r"$4x+4y=32$ (trousers)")

# Corner points of the feasible region: (0, 8), intersection of the two lines, (10, 0)
p = np.linalg.solve(M, b)
corners = np.array([[0, 8], p, [10, 0]])

# Feasible region (unbounded, shaded up to the edge of the plot window)
region = np.array([[0, 14], [0, 8], p, [10, 0], [14, 0], [14, 14]])
ax.fill(region[:, 0], region[:, 1], color="lightblue", alpha=0.5,
        label="Feasible region (unbounded)")

# Corner points with the value of Z
for px, py in corners:
    z = c @ np.array([px, py])
    ax.plot(px, py, "ko")
    ax.annotate(f"({px:.0f}, {py:.0f})\nZ = {z:.0f}", (px, py),
                textcoords="offset points", xytext=(8, 8), fontsize=9)

# Optimum and the line Z = 2700 passing through it
ax.plot(xo, yo, "ro", markersize=9,
        label=f"Minimum: Z = {zo:.0f} at ({xo:.0f}, {yo:.0f})")
ax.plot(xs, (zo - 300 * xs) / 400, "r--", linewidth=1, label=r"$300x+400y=2700$")

ax.set_xlim(-1, 14)
ax.set_ylim(-1, 14)
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.set_xlabel(r"$x$ (number of days $A$ works)")
ax.set_ylabel(r"$y$ (number of days $B$ works)")
ax.set_title(r"Minimise $Z=300x+400y$ subject to $6x+10y\geq 60,\ 4x+4y\geq 32,\ x,y\geq 0$")
ax.legend(loc="upper right", fontsize=8)
ax.grid(True)
plt.savefig("figs/tailor_cost.png", dpi=200, bbox_inches="tight")
plt.show()

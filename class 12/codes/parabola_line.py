import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Parabola 4y = 3x^2 and line 3x - 2y + 12 = 0
def parabola(x):
    return 3 * x**2 / 4

def line(x):
    return (3 * x + 12) / 2

# Intersection points: x^2 - 2x - 8 = 0
roots = np.roots([1, -2, -8])
x1, x2 = np.sort(roots)

# Area enclosed between the curves (trapezoid rule on a fine grid)
x_int = np.linspace(x1, x2, 100001)
gap = line(x_int) - parabola(x_int)
area = np.sum((gap[1:] + gap[:-1]) / 2 * np.diff(x_int))
print(f"Area = {area:.4f}")

x_vals = np.linspace(-4, 6, 400)

# Initialize single figure plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot parabola and line
ax.plot(x_vals, parabola(x_vals), color="crimson", lw=2.5, label=r"$4y=3x^2$")

# Straight line generated using line_gen
A_line = np.array([-4.0, line(-4.0)]).reshape(-1, 1)
B_line = np.array([6.0, line(6.0)]).reshape(-1, 1)
line_pts = line_gen(A_line, B_line)
ax.plot(line_pts[0, :], line_pts[1, :], color="blue", lw=2.5, label=r"$3x-2y+12=0$")

# Shade the enclosed region
ax.fill_between(x_int, parabola(x_int), line(x_int), color="orange", alpha=0.35,
                label=f"Area = {area:.0f} sq. units")

# Generate coordinate axes using line_gen
A_x = np.array([-4.0, 0.0]).reshape(-1, 1)
B_x = np.array([6.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_x, B_x)
ax.plot(x_axis[0, :], x_axis[1, :], color="black", lw=1)

A_y = np.array([0.0, -1.0]).reshape(-1, 1)
B_y = np.array([0.0, 16.0]).reshape(-1, 1)
y_axis = line_gen(A_y, B_y)
ax.plot(y_axis[0, :], y_axis[1, :], color="black", lw=1)

# Intersection points as a 2xN point matrix for label_pts
int_pts = np.block([
    np.array([x1, parabola(x1)]).reshape(-1, 1),
    np.array([x2, parabola(x2)]).reshape(-1, 1)
])
ax.plot(int_pts[0, :], int_pts[1, :], "o", color="darkred", markersize=6, zorder=5)
label_pts(int_pts, ["(-2, 3)", "(4, 12)"])

# Plot formatting
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_xlim(-4, 6)
ax.set_ylim(-1, 16)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left")

plt.tight_layout()
#If using termux
plt.savefig("figs/parabola_line.png")
#subprocess.run(shlex.split("termux-open figs/parabola_line.png"))
#else
plt.show()

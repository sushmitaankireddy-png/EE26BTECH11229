import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Function and its derivative
def f(x):
    return x**3 - 3*x**2 + 6*x - 100

def df(x):
    return 3*x**2 - 6*x + 6

x_vals = np.linspace(-3, 5, 400)

# Initialize single figure plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot f(x) and f'(x) together
ax.plot(x_vals, f(x_vals), color="crimson", lw=2.5, label=r"$f(x)=x^3-3x^2+6x-100$")
ax.plot(x_vals, df(x_vals), color="blue", lw=2.5, label=r"$f'(x)=3x^2-6x+6$")

# Generate coordinate axes using line_gen
A_x = np.array([-3.0, 0.0]).reshape(-1, 1)
B_x = np.array([5.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_x, B_x)
ax.plot(x_axis[0, :], x_axis[1, :], color="black", lw=1)

A_y = np.array([0.0, -180.0]).reshape(-1, 1)
B_y = np.array([0.0, 60.0]).reshape(-1, 1)
y_axis = line_gen(A_y, B_y)
ax.plot(y_axis[0, :], y_axis[1, :], color="black", lw=1)

# Minimum of f'(x) at x = 1 (value 3), as a 2xN point matrix for label_pts
min_pt = np.array([1.0, df(1.0)]).reshape(-1, 1)
ax.plot(min_pt[0, :], min_pt[1, :], "o", color="darkblue", markersize=6, zorder=5)
label_pts(min_pt, ["min $f'$ = 3 at x = 1"])

# Plot formatting
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x),\\ f'(x)$")
ax.set_xlim(-3, 5)
ax.set_ylim(-180, 60)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="lower right")

plt.tight_layout()
#If using termux
plt.savefig("figs/Increasing.png")
#subprocess.run(shlex.split("termux-open figs/Increasing.png"))
#else
plt.show()

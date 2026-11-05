import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Integrand: x tan x / (sec x + tan x) = x sin x / (1 + sin x)
# (simplified form avoids the 0/0 issue at x = pi/2)
def f(x):
    return x * np.sin(x) / (1 + np.sin(x))

# Limits of integration
a, b = 0.0, np.pi

# Numerical integration on a fine grid (trapezoid rule)
x_int = np.linspace(a, b, 100001)
y_int = f(x_int)
I_num = np.sum((y_int[1:] + y_int[:-1]) / 2 * np.diff(x_int))

# Exact value: I = pi*(pi - 2)/2
I_exact = np.pi * (np.pi - 2) / 2

print(f"Numerical integral : {I_num:.4f}")
print(f"Exact integral     : {I_exact:.4f}")

# Define x range for plotting
x_vals = np.linspace(0, 3.5, 500)
y_vals = f(x_vals)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot the function
ax.plot(x_vals, y_vals, 'b-', linewidth=2.5,
        label=r'$f(x) = \dfrac{x\tan x}{\sec x + \tan x}$')

# Shade the area under the curve from x = 0 to x = pi
ax.fill_between(x_int, 0, y_int, color='orange', alpha=0.35,
                label=rf'$\int_0^\pi f(x)\,dx = \dfrac{{\pi(\pi-2)}}{{2}} \approx {I_exact:.4f}$')

# Define critical points as a 2xN matrix
crit_pts = np.block([
    np.array([0.0, f(0.0)]).reshape(-1, 1),
    np.array([np.pi / 2, f(np.pi / 2)]).reshape(-1, 1),
    np.array([np.pi, f(np.pi)]).reshape(-1, 1)
])

# Highlight critical points and annotate using label_pts
ax.plot(crit_pts[0, :], crit_pts[1, :], 'ro', markersize=8, zorder=5)
label_pts(crit_pts, [r'$(0, 0)$', r'$(\pi/2, \pi/4)$', r'$(\pi, 0)$'])

# Generate vertical limit lines x = 0 and x = pi using line_gen
A_l1 = np.array([0.0, 0.0]).reshape(-1, 1)
B_l1 = np.array([0.0, 1.5]).reshape(-1, 1)
x_lim1 = line_gen(A_l1, B_l1)
ax.plot(x_lim1[0, :], x_lim1[1, :], 'r--', alpha=0.7)

A_l2 = np.array([np.pi, 0.0]).reshape(-1, 1)
B_l2 = np.array([np.pi, 1.5]).reshape(-1, 1)
x_lim2 = line_gen(A_l2, B_l2)
ax.plot(x_lim2[0, :], x_lim2[1, :], 'r--', alpha=0.7)

# Generate coordinate axes using line_gen
A_xaxis = np.array([0.0, 0.0]).reshape(-1, 1)
B_xaxis = np.array([3.5, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_xaxis, B_xaxis)
ax.plot(x_axis[0, :], x_axis[1, :], color='black', linewidth=1)

A_yaxis = np.array([0.0, 0.0]).reshape(-1, 1)
B_yaxis = np.array([0.0, 1.5]).reshape(-1, 1)
y_axis = line_gen(A_yaxis, B_yaxis)
ax.plot(y_axis[0, :], y_axis[1, :], color='black', linewidth=1)

# Labels, Grid, and Limits
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$f(x)$', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_xlim(0, 3.5)
ax.set_ylim(0, 1.5)
ax.legend(loc='upper left')

plt.tight_layout()
#if using termux
plt.savefig("figs/Integral_xtanx.png")
#subprocess.run(shlex.split("termux-open figs/Integral_xtanx.png"))
#else
plt.show()

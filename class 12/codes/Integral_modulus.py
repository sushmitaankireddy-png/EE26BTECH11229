import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Define the integrand f(x) = |x-1| + |x-2| + |x-4|
def f(x):
    return np.abs(x - 1) + np.abs(x - 2) + np.abs(x - 4)

# Limits of integration
a, b = 1.0, 4.0

# Numerical integration on a fine grid (trapezoid rule)
x_int = np.linspace(a, b, 100001)
y_int = f(x_int)
I_num = np.sum((y_int[1:] + y_int[:-1]) / 2 * np.diff(x_int))

# Exact value: f is piecewise linear with kinks at x = 1, 2, 4,
# so the trapezoid rule on these breakpoints is exact
# Define critical points as a 2xN matrix
crit_pts = np.block([
    np.array([1.0, f(1.0)]).reshape(-1, 1),
    np.array([2.0, f(2.0)]).reshape(-1, 1),
    np.array([4.0, f(4.0)]).reshape(-1, 1)
])
I_exact = np.sum((crit_pts[1, 1:] + crit_pts[1, :-1]) / 2 * np.diff(crit_pts[0, :]))

print(f"Numerical integral : {I_num:.4f}")
print(f"Exact integral     : {I_exact:.4f}")

# Define x range for plotting
x_vals = np.linspace(0, 5, 500)
y_vals = f(x_vals)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot the function
ax.plot(x_vals, y_vals, 'b-', linewidth=2.5,
        label=r'$f(x) = |x-1| + |x-2| + |x-4|$')

# Shade the area under the curve from x = 1 to x = 4
ax.fill_between(x_int, 0, y_int, color='orange', alpha=0.35,
                label=rf'$\int_1^4 f(x)\,dx = {I_exact:.1f}$')

# Highlight critical points and annotate using label_pts
ax.plot(crit_pts[0, :], crit_pts[1, :], 'ro', markersize=8, zorder=5)
label_pts(crit_pts, ['(1, 4)', '(2, 3)', '(4, 5)'])

# Generate vertical limit lines x = 1 and x = 4 using line_gen
A_l1 = np.array([1.0, 0.0]).reshape(-1, 1)
B_l1 = np.array([1.0, f(1.0)]).reshape(-1, 1)
x_lim1 = line_gen(A_l1, B_l1)
ax.plot(x_lim1[0, :], x_lim1[1, :], 'r--', alpha=0.7)

A_l2 = np.array([4.0, 0.0]).reshape(-1, 1)
B_l2 = np.array([4.0, f(4.0)]).reshape(-1, 1)
x_lim2 = line_gen(A_l2, B_l2)
ax.plot(x_lim2[0, :], x_lim2[1, :], 'r--', alpha=0.7)

# Generate coordinate axes using line_gen
A_xaxis = np.array([0.0, 0.0]).reshape(-1, 1)
B_xaxis = np.array([5.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_xaxis, B_xaxis)
ax.plot(x_axis[0, :], x_axis[1, :], color='black', linewidth=1)

A_yaxis = np.array([0.0, 0.0]).reshape(-1, 1)
B_yaxis = np.array([0.0, 7.0]).reshape(-1, 1)
y_axis = line_gen(A_yaxis, B_yaxis)
ax.plot(y_axis[0, :], y_axis[1, :], color='black', linewidth=1)

# Labels, Grid, and Limits
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$f(x)$', fontsize=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.set_xlim(0, 5)
ax.set_ylim(0, 7)
ax.legend(loc='upper center')

plt.tight_layout()
#if using termux
plt.savefig("figs/Integral_modulus.png")
#subprocess.run(shlex.split("termux-open figs/Integral_modulus.png"))
#else
plt.show()

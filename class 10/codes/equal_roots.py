import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Quadratic from the solution: x^2 + 4x + 4 = 0
p = np.array([1.0, 4.0, 4.0])

# Roots of the quadratic
roots = np.unique(np.round(np.real(np.roots(p)), 6))
print("Roots =", roots)
print("Discriminant =", p[1]**2 - 4 * p[0] * p[2])

# Parabola y = x^2 + 4x + 4 generated as 2 x N points
x = np.linspace(-6, 2, 200)
y = np.polyval(p, x)
x_parab = np.vstack((x, y))

# x axis using line_gen
X1 = np.array([-6.0, 0.0]).reshape(-1, 1)
X2 = np.array([2.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(X1, X2)

# Intersection points of the parabola with the x axis (y = 0)
R = np.vstack((roots, np.polyval(p, roots)))
print("Intersection points with x axis =", R.T)

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_parab[0, :], x_parab[1, :], label=r'$y = x^2 + 4x + 4$')
ax.plot(x_axis[0, :], x_axis[1, :], 'k-', label='$x$ axis')

# Labeling the intersection points
ax.scatter(R[0, :], R[1, :], color='r', zorder=5)
label_pts(R, [f'({r:g}, 0)' for r in roots])

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='best')
ax.grid(True)

plt.tight_layout()
#If using termux
plt.savefig("figs/equal_roots.png")
#subprocess.run(shlex.split("termux-open figs/equal_roots.png"))
#else
plt.show()

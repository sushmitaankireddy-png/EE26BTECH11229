import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Roots are alpha and 6 alpha: 7 alpha = 14/p, 6 alpha^2 = 8/p
# alpha = 2/p, 24/p^2 = 8/p
p = 24 / 8
print("p =", p)

# Parabola y = p x^2 - 14 x + 8 in the form x^T V x + 2 u^T x + f = 0
V = np.array([[p, 0.0], [0.0, 0.0]])
u = np.array([-7.0, -0.5]).reshape(-1, 1)
f = 8.0
print("V =", V.tolist(), ", u =", u.flatten(), ", f =", f)
print("rank(V) =", np.linalg.matrix_rank(V))

# Parabola points from the quadratic form, solving for y
x = np.linspace(-1, 5, 200)
y = -(V[0, 0] * x**2 + 2 * u[0, 0] * x + f) / (2 * u[1, 0])
x_parab = np.vstack((x, y))

# x axis: x = h + k m
h = np.array([0.0, 0.0]).reshape(-1, 1)
m = np.array([1.0, 0.0]).reshape(-1, 1)

# Intersection with the x axis:
# (m^T V m) k^2 + 2 m^T (V h + u) k + g(h) = 0
a2 = (m.T @ V @ m).item()
a1 = 2 * (m.T @ (V @ h + u)).item()
a0 = (h.T @ V @ h).item() + 2 * (u.T @ h).item() + f
print("m^T V m =", a2, ", 2 m^T(Vh+u) =", a1, ", g(h) =", a0)

k = np.sort(np.roots([a2, a1, a0]))
print("k =", k)

# Intersection points
R = h + m * k
print("Intersection points =", R.T)

# Roots of the given quadratic p x^2 - 14 x + 8 = 0
roots = np.sort(np.roots([p, -14.0, 8.0]))
print("Roots of the quadratic =", roots)
print("Roots = x coordinates of intersection points:", np.allclose(roots, R[0, :]))

# Check that the points satisfy the quadratic form
for i in range(R.shape[1]):
    P = R[:, i].reshape(-1, 1)
    print("x^T V x + 2 u^T x + f =", (P.T @ V @ P).item() + 2 * (u.T @ P).item() + f)

# x axis using line_gen
X1 = np.array([-1.0, 0.0]).reshape(-1, 1)
X2 = np.array([5.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(X1, X2)

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_parab[0, :], x_parab[1, :], label=r'$y = 3x^2 - 14x + 8$')
ax.plot(x_axis[0, :], x_axis[1, :], 'k-', label='$x$ axis')

# Labeling the intersection points
ax.scatter(R[0, :], R[1, :], color='r', zorder=5)
label_pts(R, [f'({r:.3g}, 0)' for r in R[0, :]])

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.legend(loc='best')
ax.grid(True)

plt.tight_layout()
#If using termux
plt.savefig("figs/root_ratio.png")
#subprocess.run(shlex.split("termux-open figs/root_ratio.png"))
#else
plt.show()

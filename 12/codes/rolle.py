import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# f(x) = x^3 - 3x with coefficients, f'(x) = 3x^2 - 3
p = np.array([1.0, 0.0, -3.0, 0.0])
dp = np.polyder(p)

# End points of the interval [a, b], f(a) = f(b) = 0
a = -np.sqrt(3)
b = 0.0
print("f(a), f(b) =", np.polyval(p, a), np.polyval(p, b))

# Rolle's theorem: f'(c) = 0 for some c in (a, b)
croots = np.roots(dp)
c = croots[(croots > a) & (croots < b)].item()
print("c =", c, ", f'(c) =", np.polyval(dp, c))

# Points on the curve
A = np.array([a, np.polyval(p, a)]).reshape(-1, 1)
B = np.array([b, np.polyval(p, b)]).reshape(-1, 1)
C = np.array([c, np.polyval(p, c)]).reshape(-1, 1)
print("A =", A.flatten(), ", B =", B.flatten(), ", C =", C.flatten())

# Curve generated as 2 x N points
x = np.linspace(-2, 0.5, 400)
x_curve = np.vstack((x, np.polyval(p, x)))

# Chord joining A and B
x_AB = line_gen(A, B)

# Tangent at C (horizontal, since f'(c) = 0)
m = np.array([1.0, np.polyval(dp, c)]).reshape(-1, 1)
T1 = C - 0.7 * m
T2 = C + 0.7 * m
x_tan = line_gen(T1, T2)

# Coordinate axes
X1 = np.array([-2.0, 0.0]).reshape(-1, 1)
X2 = np.array([0.5, 0.0]).reshape(-1, 1)
Y1 = np.array([0.0, -2.5]).reshape(-1, 1)
Y2 = np.array([0.0, 2.5]).reshape(-1, 1)
x_xaxis = line_gen(X1, X2)
x_yaxis = line_gen(Y1, Y2)

# Plotting
plt.plot(x_curve[0, :], x_curve[1, :], label=r'$f(x)=x^3-3x$')
plt.plot(x_AB[0, :], x_AB[1, :], 'g--', label='Chord $AB$')
plt.plot(x_tan[0, :], x_tan[1, :], 'r--', label=r"Tangent at $c=-1$: $f'(c)=0$")
plt.plot(x_xaxis[0, :], x_xaxis[1, :], 'k-', linewidth=0.8)
plt.plot(x_yaxis[0, :], x_yaxis[1, :], 'k-', linewidth=0.8)

# Labeling the coordinates
tri_coords = np.block([A, B, C])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = [r'$A(-\sqrt{3},0)$', '$B(0,0)$', '$C(-1,2)$']
label_pts(tri_coords, vert_labels)

plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title(r"Rolle's theorem for $f(x)=x^3-3x$ on $[-\sqrt{3},\,0]$")
plt.legend(loc='lower left')
plt.grid()

plt.tight_layout()
#If using termux
plt.savefig("figs/rolle.png")
#subprocess.run(shlex.split("termux-open figs/rolle.png"))
#else
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Given points
A = np.array([5.0, 1.0]).reshape(-1, 1)
B = np.array([-1.0, 5.0]).reshape(-1, 1)

# Locus of P: ||P - A|| = ||P - B||  =>  (A - B)^T P = (||A||^2 - ||B||^2)/2
n = A - B
c = (np.linalg.norm(A)**2 - np.linalg.norm(B)**2) / 2
print("n =", n.flatten())
print("||A||^2, ||B||^2 =", np.linalg.norm(A)**2, np.linalg.norm(B)**2)
print(f"{n[0,0]}x + ({n[1,0]})y = {c}")

# Direction vector of the line and a point on it
Rot = np.array([[0, 1], [-1, 0]])
m = Rot @ n
P0 = c * n / np.linalg.norm(n)**2

# Two points on the line 3x = 2y
P1 = P0 + 2 * m
P2 = P0 - 2 * m

# Check with a point P on the line
P = P0 + 0.5 * m
print("||P - A||, ||P - B|| =", np.linalg.norm(P - A), np.linalg.norm(P - B))

# Generating the lines
x_AB = line_gen(A, B)
x_PP = line_gen(P1, P2)
x_PA = line_gen(P, A)
x_PB = line_gen(P, B)

# Plotting
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_PP[0, :], x_PP[1, :], label='$3x = 2y$')
plt.plot(x_PA[0, :], x_PA[1, :], label='$PA$')
plt.plot(x_PB[0, :], x_PB[1, :], label='$PB$')

# Labeling the coordinates
tri_coords = np.block([A, B, P])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'P']
label_pts(tri_coords, vert_labels)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.tight_layout()
#If using termux
plt.savefig("figs/perp_bisector.png")
#subprocess.run(shlex.split("termux-open figs/perp_bisector.png"))
#else
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Circle with centre O and radius r
r = 10.0
O = np.array([0.0, 0.0]).reshape(-1, 1)

# Points of contact P, Q, C
P = np.array([0.0, r]).reshape(-1, 1)
Q = np.array([0.0, -r]).reshape(-1, 1)
C = np.array([8.0, -6.0]).reshape(-1, 1)
print("||C||^2 =", (C.T @ C).item(), ", r^2 =", r**2)

# A lies on y = 10 and B lies on y = -10
# A^T C = r^2, B^T C = r^2
a = (r**2 - r * C[1, 0]) / C[0, 0]
b = (r**2 + r * C[1, 0]) / C[0, 0]
A = np.array([a, r]).reshape(-1, 1)
B = np.array([b, -r]).reshape(-1, 1)
print("A =", A.flatten(), ", B =", B.flatten())
print("ab =", a * b, ", r^2 =", r**2)

# AB is perpendicular to the radius at C
print("(A - C)^T C =", ((A - C).T @ C).item())
print("(B - C)^T C =", ((B - C).T @ C).item())

# Tangent lengths from A and B are equal
print("||A - P||, ||A - C|| =", np.linalg.norm(A - P), np.linalg.norm(A - C))
print("||B - Q||, ||B - C|| =", np.linalg.norm(B - Q), np.linalg.norm(B - C))

# Angle AOB
cos_AOB = (A.T @ B).item() / (np.linalg.norm(A) * np.linalg.norm(B))
print("cos(AOB) =", cos_AOB)
print("Angle AOB =", np.degrees(np.arccos(cos_AOB)), "degrees")

# Generating the lines and the circle
X = np.array([-r - 5, r]).reshape(-1, 1)
Y = np.array([a + 5, r]).reshape(-1, 1)
X1 = np.array([-r - 5, -r]).reshape(-1, 1)
Y1 = np.array([a + 5, -r]).reshape(-1, 1)

x_XY = line_gen(X, Y)
x_X1Y1 = line_gen(X1, Y1)
x_AB = line_gen(A, B)
x_OA = line_gen(O, A)
x_OB = line_gen(O, B)
x_OC = line_gen(O, C)
x_PQ = line_gen(P, Q)
x_circ = circ_gen(O, r)

# Plotting
plt.plot(x_XY[0, :], x_XY[1, :], label='$XY$')
plt.plot(x_X1Y1[0, :], x_X1Y1[1, :], label="$X'Y'$")
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_OA[0, :], x_OA[1, :], label='$OA$')
plt.plot(x_OB[0, :], x_OB[1, :], label='$OB$')
plt.plot(x_OC[0, :], x_OC[1, :], 'k--')
plt.plot(x_PQ[0, :], x_PQ[1, :], 'k-')
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')

# Labeling the coordinates
tri_coords = np.block([O, P, Q, C, A, B])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['O', 'P', 'Q', 'C', 'A', 'B']
label_pts(tri_coords, vert_labels)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.tight_layout()
#If using termux
plt.savefig("figs/tangent_angle.png")
#subprocess.run(shlex.split("termux-open figs/tangent_angle.png"))
#else
plt.show()

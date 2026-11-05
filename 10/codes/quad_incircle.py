import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.plotting.funcs import label_pts

# Vertices of the quadrilateral ABCD
A = np.array([0.0, 0.0]).reshape(-1, 1)
B = np.array([6.0, 0.0]).reshape(-1, 1)
C = np.array([3.0, 4.0]).reshape(-1, 1)
D = np.array([0.0, 4.0]).reshape(-1, 1)

# Side lengths
AB = np.linalg.norm(B - A)
BC = np.linalg.norm(C - B)
CD = np.linalg.norm(D - C)
DA = np.linalg.norm(A - D)
print("AB, BC, CD, DA =", AB, BC, CD, DA)
print("AB + CD =", AB + CD, ", BC + DA =", BC + DA)

# Angle bisector directions at A and B
m_A = (B - A) / AB + (D - A) / DA
m_B = (A - B) / AB + (C - B) / BC
m_B = m_B / m_B[1]

# O = A + t m_A = B + s m_B
M = np.hstack((m_A, -m_B))
t, s = np.linalg.solve(M, (B - A).flatten())
O = A + t * m_A

# Radius = distance of O from side AB
Rot = np.array([[0, 1], [-1, 0]])
n1 = Rot @ (B - A)
r = abs((n1.T @ (O - A)).item()) / np.linalg.norm(n1)

print("t, s =", t, s)
print("O =", O.flatten())
print("r =", r)

# Generating the sides and the circle
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)
x_CD = line_gen(C, D)
x_DA = line_gen(D, A)
x_circ = circ_gen(O, r)

# Plotting
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$')
plt.plot(x_CD[0, :], x_CD[1, :], label='$CD$')
plt.plot(x_DA[0, :], x_DA[1, :], label='$DA$')
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')

# Labeling the coordinates
tri_coords = np.block([A, B, C, D, O])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['A', 'B', 'C', 'D', 'O']
label_pts(tri_coords, vert_labels)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.tight_layout()
#If using termux
plt.savefig("figs/quad_incircle.png")
#subprocess.run(shlex.split("termux-open figs/quad_incircle.png"))
#else
plt.show()

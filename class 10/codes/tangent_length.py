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

# Circle with centre O and radius a
a = 3.0
O = np.array([0.0, 0.0]).reshape(-1, 1)

# Angle between the tangents is 60 degrees, so angle OPT1 = 30 degrees
ang = np.radians(60.0)
OP = a / np.sin(ang / 2)
print("||O - P|| =", OP, ", 2a =", 2 * a)

# P on the x axis
P = np.array([OP, 0.0]).reshape(-1, 1)

# Points of contact T1 and T2, with ||O - T|| = a and angle POT = 90 - 30 = 60 degrees
th = np.pi / 2 - ang / 2
T1 = a * np.array([np.cos(th), np.sin(th)]).reshape(-1, 1)
T2 = a * np.array([np.cos(th), -np.sin(th)]).reshape(-1, 1)
print("T1 =", T1.flatten(), ", T2 =", T2.flatten())

# Tangent lengths are equal
print("||P - T1||, ||P - T2|| =", np.linalg.norm(P - T1), np.linalg.norm(P - T2))

# Triangle OT1P is right angled at T1
print("(P - T1)^T (T1 - O) =", ((P - T1).T @ (T1 - O)).item())

# Angle between the tangents at P
cos_P = ((T1 - P).T @ (T2 - P)).item() / (np.linalg.norm(T1 - P) * np.linalg.norm(T2 - P))
print("Angle T1 P T2 =", np.degrees(np.arccos(cos_P)), "degrees")

# Angle OPT1
cos_OPT = ((O - P).T @ (T1 - P)).item() / (np.linalg.norm(O - P) * np.linalg.norm(T1 - P))
print("Angle OPT1 =", np.degrees(np.arccos(cos_OPT)), "degrees")

# sin 30 = a / ||O - P||
print("sin 30 =", np.sin(np.radians(30.0)), ", a/||O - P|| =", a / np.linalg.norm(O - P))

# Generating the lines and the circle
x_PT1 = line_gen(P, T1)
x_PT2 = line_gen(P, T2)
x_OT1 = line_gen(O, T1)
x_OT2 = line_gen(O, T2)
x_OP = line_gen(O, P)
x_circ = circ_gen(O, a)

# Plotting
plt.plot(x_PT1[0, :], x_PT1[1, :], label='$PT_1$')
plt.plot(x_PT2[0, :], x_PT2[1, :], label='$PT_2$')
plt.plot(x_OT1[0, :], x_OT1[1, :], label='$OT_1$')
plt.plot(x_OT2[0, :], x_OT2[1, :], label='$OT_2$')
plt.plot(x_OP[0, :], x_OP[1, :], label='$OP$')
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')

# Labeling the coordinates
tri_coords = np.block([O, P, T1, T2])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['O', 'P', '$T_1$', '$T_2$']
label_pts(tri_coords, vert_labels)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.tight_layout()
#If using termux
plt.savefig("figs/tangent_length.png")
#subprocess.run(shlex.split("termux-open figs/tangent_length.png"))
#else
plt.show()

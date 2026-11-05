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

# Circle with centre O and radius r, external point h
r = 5.0
O = np.array([0.0, 0.0]).reshape(-1, 1)
h = np.array([5.0, 10.0]).reshape(-1, 1)

# Circle in the form x^T V x + 2 u^T x + f = 0
V = np.eye(2)
u = -O
f = (O.T @ O).item() - r**2
print("V =", V.tolist(), ", u =", u.flatten(), ", f =", f)

# g(h) > 0 means h is an external point
g = (h.T @ V @ h).item() + 2 * (u.T @ h).item() + f
print("g(h) =", g)

# Sigma = (Vh + u)(Vh + u)^T - g(h) V
Vhu = V @ h + u
Sigma = Vhu @ Vhu.T - g * V
print("Sigma =", Sigma.tolist())

# Eigenvalues and eigenvectors, lambda1 > 0 > lambda2
lam, P = np.linalg.eigh(Sigma)
idx = np.argsort(-lam)
lam = lam[idx]
P = P[:, idx]
print("Eigenvalues =", lam)
print("P^T P =", (P.T @ P).tolist())
print("P^T Sigma P =", (P.T @ Sigma @ P).round(6).tolist())

# Direction vectors of the tangents, m = P (sqrt(-lambda2), +-sqrt(lambda1))
m1 = P @ np.array([np.sqrt(-lam[1]), np.sqrt(lam[0])]).reshape(-1, 1)
m2 = P @ np.array([np.sqrt(-lam[1]), -np.sqrt(lam[0])]).reshape(-1, 1)
print("m1 =", m1.flatten(), ", m2 =", m2.flatten())

# Points of contact T = h + mu m, mu = -m^T (Vh + u) / (m^T V m)
mu1 = -(m1.T @ Vhu).item() / (m1.T @ V @ m1).item()
mu2 = -(m2.T @ Vhu).item() / (m2.T @ V @ m2).item()
T1 = h + mu1 * m1
T2 = h + mu2 * m2
print("mu1, mu2 =", mu1, mu2)
print("T1 =", T1.flatten(), ", T2 =", T2.flatten())

# Both points lie on the circle
print("||T1 - O||, ||T2 - O|| =", np.linalg.norm(T1 - O), np.linalg.norm(T2 - O))

# Tangents are perpendicular to the radii
print("(h - T1)^T (T1 - O) =", ((h - T1).T @ (T1 - O)).item())
print("(h - T2)^T (T2 - O) =", ((h - T2).T @ (T2 - O)).item())

# Lengths of the tangents
print("||h - T1||, ||h - T2|| =", np.linalg.norm(h - T1), np.linalg.norm(h - T2))
print("sqrt(||h - O||^2 - r^2) =", np.sqrt(np.linalg.norm(h - O)**2 - r**2))

# Generating the lines and the circle
x_hT1 = line_gen(h, T1)
x_hT2 = line_gen(h, T2)
x_OT1 = line_gen(O, T1)
x_OT2 = line_gen(O, T2)
x_Oh = line_gen(O, h)
x_circ = circ_gen(O, r)

# Plotting
plt.plot(x_hT1[0, :], x_hT1[1, :], label='$hT_1$')
plt.plot(x_hT2[0, :], x_hT2[1, :], label='$hT_2$')
plt.plot(x_OT1[0, :], x_OT1[1, :], label='$OT_1$')
plt.plot(x_OT2[0, :], x_OT2[1, :], label='$OT_2$')
plt.plot(x_Oh[0, :], x_Oh[1, :], 'k--')
plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')

# Labeling the coordinates
tri_coords = np.block([O, h, T1, T2])
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['O', 'h', '$T_1$', '$T_2$']
label_pts(tri_coords, vert_labels)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

plt.tight_layout()
#If using termux
plt.savefig("figs/tangent_equal.png")
#subprocess.run(shlex.split("termux-open figs/tangent_equal.png"))
#else
plt.show()

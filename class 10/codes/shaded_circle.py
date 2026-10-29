import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

# Import custom matrix and vector modules
from CoordGeo.conics.funcs import circ_gen
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Initialize figure
fig, ax = plt.subplots(figsize=(9, 6), layout='constrained')

# Parameters
AB = 7.0
AC = 24.0
BC = np.sqrt(AB**2 + AC**2)    # angle BAC = 90 deg, so BC is a diameter
R = BC / 2

# Points (O at origin, BC along x-axis)
O = np.array([0.0, 0.0]).reshape(-1, 1)
B = np.array([R, 0.0]).reshape(-1, 1)
C = np.array([-R, 0.0]).reshape(-1, 1)
D = np.array([0.0, -R]).reshape(-1, 1)
cosB = AB / BC
sinB = AC / BC
A = B + AB * np.array([-cosB, sinB]).reshape(-1, 1)

# 1. Circle
x_circ = circ_gen(O, R)
ax.plot(x_circ[0, :], x_circ[1, :], 'k-', linewidth=2)

# 2. Segment cut off by chord AC (shaded)
x_seg = x_circ[:, (x_circ[1, :] > 0) & (x_circ[0, :] < A[0, 0])]
x_seg = np.block([A, x_seg, C])
ax.fill(x_seg[0, :], x_seg[1, :], color='#a6d5ff', alpha=0.8)

# 3. Segment cut off by chord AB (shaded)
x_seg2 = x_circ[:, (x_circ[1, :] > 0) & (x_circ[0, :] > A[0, 0])]
x_seg2 = np.block([B, x_seg2, A])
ax.fill(x_seg2[0, :], x_seg2[1, :], color='#a6d5ff', alpha=0.8)

# 4. Sector BOD (shaded)
x_sec = x_circ[:, (x_circ[0, :] > 0) & (x_circ[1, :] < 0)]
x_sec = np.block([O, D, x_sec, B])
ax.fill(x_sec[0, :], x_sec[1, :], color='#fcaeae', alpha=0.7)

# 5. Lines AB, AC, BC, OD
x_AB = line_gen(A, B)
x_AC = line_gen(A, C)
x_BC = line_gen(B, C)
x_OD = line_gen(O, D)
ax.plot(x_AB[0, :], x_AB[1, :], 'k-', linewidth=1.5)
ax.plot(x_AC[0, :], x_AC[1, :], 'k-', linewidth=1.5)
ax.plot(x_BC[0, :], x_BC[1, :], 'k-', linewidth=1.5)
ax.plot(x_OD[0, :], x_OD[1, :], 'k-', linewidth=1.5)

# 6. Points & Labeling
pts = np.block([O, A, B, C, D])
ax.plot(pts[0, :], pts[1, :], 'ko', markersize=5, zorder=5)
label_pts(pts, ['O', 'A', 'B', 'C', 'D'])

# Area of shaded region
# segment on AC = (1/2) R^2 (theta - sin(theta)), theta = angle AOC = 2*angle B
# segment on AB = (1/2) R^2 (phi - sin(phi)),     phi = angle AOB = 2*angle C
# sector BOD = (1/4) pi R^2
theta = 2 * np.arctan(AC / AB)
phi = 2 * np.arctan(AB / AC)
area_seg = 0.5 * R**2 * (theta - np.sin(theta))
area_seg2 = 0.5 * R**2 * (phi - np.sin(phi))
area_sec = 0.25 * np.pi * R**2
area = area_seg + area_seg2 + area_sec
# same as: semicircle - triangle ABC + sector BOD
print("Radius =", R, "cm")
print("Area of shaded region =", round(area, 4), "cm^2")
print("Area of shaded region (pi = 22/7) =", round((22/7) * R**2 * 0.75 - 0.5 * AB * AC, 4), "cm^2")

# Formatting plot area
ax.set_xlim(-14, 14)
ax.set_ylim(-14, 14)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')

#If using termux
plt.savefig('figs/shaded_circle.png')
#subprocess.run(shlex.split("termux-open figs/shaded_circle.png"))

#else
plt.show()

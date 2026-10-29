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
R = 4.5
r = 1.5
rc = 2.25

O = np.array([0.0, 0.0]).reshape(-1, 1)
C = np.array([0.0, rc]).reshape(-1, 1)
P = np.array([-3.0, 0.0]).reshape(-1, 1)
Q = np.array([3.0, 0.0]).reshape(-1, 1)
e = np.array([r, 0.0]).reshape(-1, 1)

# 1. Big semicircle (upper half of circle)
x_big = circ_gen(O, R)
x_big = x_big[:, x_big[1, :] > 0]
x_big = np.block([O + R * e / r, x_big, O - R * e / r])
ax.plot(x_big[0, :], x_big[1, :], 'k-', linewidth=2)
ax.fill(x_big[0, :], x_big[1, :], color='#a6d5ff', alpha=0.8)

# 2. Circle of diameter 4.5 cm (not shaded)
x_circ = circ_gen(C, rc)
ax.fill(x_circ[0, :], x_circ[1, :], color='white', zorder=3)
ax.plot(x_circ[0, :], x_circ[1, :], 'r-', linewidth=1.5, zorder=4)

# 3. Left and right semicircles (not shaded)
x_left = circ_gen(P, r)
x_left = x_left[:, x_left[1, :] > 0]
x_left = np.block([P + e, x_left, P - e])
ax.fill(x_left[0, :], x_left[1, :], color='white', zorder=3)
ax.plot(x_left[0, :], x_left[1, :], 'g-', linewidth=1.5, zorder=4)

x_right = circ_gen(Q, r)
x_right = x_right[:, x_right[1, :] > 0]
x_right = np.block([Q + e, x_right, Q - e])
ax.fill(x_right[0, :], x_right[1, :], color='white', zorder=3)
ax.plot(x_right[0, :], x_right[1, :], 'g-', linewidth=1.5, zorder=4)

# 4. Lower semicircle (shaded)
x_low = circ_gen(O, r)
x_low = x_low[:, x_low[1, :] < 0]
x_low = np.block([O - e, x_low, O + e])
ax.fill(x_low[0, :], x_low[1, :], color='#a6d5ff', alpha=0.8, zorder=3)
ax.plot(x_low[0, :], x_low[1, :], 'g-', linewidth=1.5, zorder=4)

# 5. Diameter line
A = np.array([-R, 0.0]).reshape(-1, 1)
B = np.array([R, 0.0]).reshape(-1, 1)
x_AB = line_gen(A, B)
ax.plot(x_AB[0, :], x_AB[1, :], 'k-', linewidth=2, zorder=5)

# 6. Center Points & Labeling
centers = np.block([O, C, P, Q])
ax.plot(centers[0, :], centers[1, :], 'ko', markersize=5, zorder=6)
label_pts(centers, ['O', 'C', 'P', 'Q'])

# Area of shaded region
# big semicircle - circle - 2 small semicircles + lower semicircle
area = 0.5*np.pi*R**2 - np.pi*rc**2 - 2*(0.5*np.pi*r**2) + 0.5*np.pi*r**2
print("Area of shaded region =", round(area, 4), "cm^2")

# Formatting plot area
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')

#If using termux
plt.savefig('figs/shaded_region.png')
#subprocess.run(shlex.split("termux-open figs/shaded_region.png"))

#else
plt.show()

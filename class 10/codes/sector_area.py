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
r = 21.0                  # radius of inner circle
R = 42.0                  # radius of outer circle
ang = np.deg2rad(60)      # angle AOB
a1 = np.deg2rad(270) - ang / 2    # direction of OA
a2 = np.deg2rad(270) + ang / 2    # direction of OB

O = np.array([0.0, 0.0]).reshape(-1, 1)
A = R * np.array([np.cos(a1), np.sin(a1)]).reshape(-1, 1)
B = R * np.array([np.cos(a2), np.sin(a2)]).reshape(-1, 1)
C = r * np.array([np.cos(a1), np.sin(a1)]).reshape(-1, 1)
D = r * np.array([np.cos(a2), np.sin(a2)]).reshape(-1, 1)

# 1. Outer circle (shaded)
x_out = circ_gen(O, R)
ax.fill(x_out[0, :], x_out[1, :], color='#a6d5ff', alpha=0.8)
ax.plot(x_out[0, :], x_out[1, :], 'b-', linewidth=2, zorder=4)

# 2. Sector OAB (not shaded)
x_sec = x_out[:, (x_out[1, :] < 0) & (np.abs(x_out[0, :]) < -x_out[1, :] * np.tan(ang / 2))]
x_sec = np.block([O, A, x_sec, B])
ax.fill(x_sec[0, :], x_sec[1, :], color='white', zorder=2)

# 3. Inner circle (not shaded)
x_in = circ_gen(O, r)
ax.fill(x_in[0, :], x_in[1, :], color='white', zorder=2)
ax.plot(x_in[0, :], x_in[1, :], 'r-', linewidth=2, zorder=4)

# 4. Radii OA and OB
x_OA = line_gen(O, A)
x_OB = line_gen(O, B)
ax.plot(x_OA[0, :], x_OA[1, :], 'k-', linewidth=1.5, zorder=4)
ax.plot(x_OB[0, :], x_OB[1, :], 'k-', linewidth=1.5, zorder=4)

# 5. Points & Labeling
pts = np.block([O, A, B, C, D])
ax.plot(pts[0, :], pts[1, :], 'ko', markersize=5, zorder=5)
label_pts(pts, ['O', 'A', 'B', 'C', 'D'])

# Area of shaded region
# shaded = ring area * (360 - 60)/360
pi = 22 / 7
area = pi * (R**2 - r**2) * (360 - 60) / 360
print("Area of shaded region (pi = 22/7) =", round(area, 4), "cm^2")
print("Area of shaded region (exact pi) =", round(np.pi * (R**2 - r**2) * 300 / 360, 4), "cm^2")

# Formatting plot area
ax.set_xlim(-48, 48)
ax.set_ylim(-48, 48)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(False)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')

#If using termux
plt.savefig('figs/sector_area.png')
#subprocess.run(shlex.split("termux-open figs/sector_area.png"))

#else
plt.show()

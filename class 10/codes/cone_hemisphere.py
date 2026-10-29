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
r = 3.5            # radius of cone and hemisphere
H = 15.5           # total height of the toy
h = H - r          # height of the cone
l = np.sqrt(h**2 + r**2)   # slant height of the cone

# Points (O is the centre of the common circular face)
O = np.array([0.0, 0.0]).reshape(-1, 1)
A = np.array([0.0, h]).reshape(-1, 1)      # apex of the cone
B = np.array([r, 0.0]).reshape(-1, 1)
C = np.array([-r, 0.0]).reshape(-1, 1)
D = np.array([0.0, -r]).reshape(-1, 1)     # bottom of the hemisphere

# 1. Hemisphere (lower half of circle)
x_hemi = circ_gen(O, r)
x_hemi = x_hemi[:, x_hemi[1, :] < 0]
x_hemi = np.block([C, x_hemi, B])
ax.plot(x_hemi[0, :], x_hemi[1, :], 'b-', linewidth=2)
ax.fill(x_hemi[0, :], x_hemi[1, :], color='#a6d5ff', alpha=0.8)

# 2. Cone (triangle ABC)
x_AB = line_gen(A, B)
x_AC = line_gen(A, C)
x_BC = line_gen(B, C)
ax.plot(x_AB[0, :], x_AB[1, :], 'r-', linewidth=2)
ax.plot(x_AC[0, :], x_AC[1, :], 'r-', linewidth=2)
ax.plot(x_BC[0, :], x_BC[1, :], 'k--', linewidth=1.5)
ax.fill([A[0, 0], B[0, 0], C[0, 0]], [A[1, 0], B[1, 0], C[1, 0]], color='#fcaeae', alpha=0.7)

# 3. Height AO (dashed)
x_AO = line_gen(A, O)
ax.plot(x_AO[0, :], x_AO[1, :], 'k--', linewidth=1.5)

# 4. Points & Labeling
pts = np.block([O, A, B, C, D])
ax.plot(pts[0, :], pts[1, :], 'ko', markersize=5)
label_pts(pts, ['O', 'A', 'B', 'C', 'D'])

# Total surface area = curved surface of cone + curved surface of hemisphere
# TSA = pi*r*l + 2*pi*r^2
csa_cone = np.pi * r * l
csa_hemi = 2 * np.pi * r**2
tsa = csa_cone + csa_hemi
print("Height of cone h =", h, "cm")
print("Slant height l =", l, "cm")
print("Total surface area =", round(tsa, 4), "cm^2")
print("Total surface area (pi = 22/7) =", round(22/7 * r * (l + 2*r), 4), "cm^2")

# Formatting plot area
ax.set_xlim(-6, 6)
ax.set_ylim(-5, 14)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')

#If using termux
plt.savefig('figs/cone_hemisphere.png')
#subprocess.run(shlex.split("termux-open figs/cone_hemisphere.png"))

#else
plt.show()

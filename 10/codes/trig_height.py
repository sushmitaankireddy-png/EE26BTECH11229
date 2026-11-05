import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Define distances and calculate the tower height
d1 = 4
d2 = 16
height = np.sqrt(d1 * d2)

A = np.array([0, 0])
B = np.array([d1, 0])
C = np.array([d2, 0])
D = np.array([0, height])

plt.figure(figsize=(8, 5))

# Draw the baseline and dashed projection lines
plt.plot([0, d2], [0, 0], 'k-')
plt.plot([0, 0], [0, height], 'k-')
plt.plot([d1, 0], [0, height], 'b--')
plt.plot([d2, 0], [0, height], 'r--')

plt.scatter([0, d1, d2], [height, 0, 0])

# Add labels for dimensions
plt.text(-0.5, height / 2, f'{height:.0f} m')
plt.text(d1, -0.5, '4 m', ha='center')
plt.text(d2, -0.5, '16 m', ha='center')

plt.title('Height of the Tower')
plt.xlabel('Horizontal distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.axis('equal')

plt.savefig("figs/trig_height.png")
plt.show()

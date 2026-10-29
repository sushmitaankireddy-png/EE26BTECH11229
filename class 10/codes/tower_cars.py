import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Define tower height and angles of depression/elevation
height = 100
angle1 = np.radians(30)
angle2 = np.radians(45)

# Calculate distances of the cars from the base of the tower
d1 = height / np.tan(angle1)
d2 = height / np.tan(angle2)
total_distance = d1 + d2

print("Distance of first car =", round(d1, 2), "m")
print("Distance of second car =", round(d2, 2), "m")
print("Distance between the cars =", round(total_distance, 2), "m")

fig, ax = plt.subplots(figsize=(9, 5))

# Plot the tower and the ground line
ax.plot([0, 0], [0, height], 'k-', linewidth=2)
ax.plot([-d2, d1], [0, 0], 'k-')

# Plot lines of sight to the cars
ax.plot([-d2, 0], [0, height], 'b--')
ax.plot([d1, 0], [0, height], 'r--')

ax.scatter([-d2, 0, d1], [0, height, 0])

# Add text labels for cars, height, and angles
ax.text(-d2, -5, 'Car B', ha='center')
ax.text(d1, -5, 'Car A', ha='center')
ax.text(2, height / 2, '100 m')

ax.text(-d2 / 2, height / 2, '45°')
ax.text(d1 / 2, height / 2, '30°')

ax.set_title('Tower and Two Cars')
ax.set_xlabel('Horizontal distance (m)')
ax.set_ylabel('Height (m)')
ax.grid(True)

plt.savefig("figs/tower_cars.png")
plt.show()

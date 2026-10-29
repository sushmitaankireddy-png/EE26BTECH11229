import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# All ways of drawing 2 cards from {1, 3, 5, 7} without replacement
cards = [1, 3, 5, 7]
sums = np.array([a + b for a, b in combinations(cards, 2)])

# PMF of X = sum of the two cards
x_vals = np.unique(sums)
p_vals = np.array([np.sum(sums == x) / len(sums) for x in x_vals])

# Mean and variance
mean = np.sum(x_vals * p_vals)
var = np.sum(x_vals**2 * p_vals) - mean**2
print("X      :", x_vals)
print("P(X)   :", np.round(p_vals, 4))
print(f"Mean     = {mean:.4f}")
print(f"Variance = {var:.4f}")

# PMF points as a 2xN matrix for label_pts
pmf_pts = np.block([[x_vals], [p_vals]])

# Initialize single figure plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw each PMF stem using line_gen
for i in range(len(x_vals)):
    A = np.array([x_vals[i], 0.0]).reshape(-1, 1)
    B = np.array([x_vals[i], p_vals[i]]).reshape(-1, 1)
    stem = line_gen(A, B)
    ax.plot(stem[0, :], stem[1, :], color="crimson", lw=2.5)

# Plot and label the PMF points
ax.plot(pmf_pts[0, :], pmf_pts[1, :], "o", color="darkred", markersize=7, zorder=5)
label_pts(pmf_pts, ["1/6", "1/6", "2/6", "1/6", "1/6"])

# Baseline axis using line_gen
A_x = np.array([2.0, 0.0]).reshape(-1, 1)
B_x = np.array([14.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_x, B_x)
ax.plot(x_axis[0, :], x_axis[1, :], color="black", lw=1)

# Mean marked with a dashed vertical line using line_gen
A_m = np.array([mean, 0.0]).reshape(-1, 1)
B_m = np.array([mean, 0.4]).reshape(-1, 1)
m_line = line_gen(A_m, B_m)
ax.plot(m_line[0, :], m_line[1, :], color="blue", linestyle="--", lw=1.5,
        label=rf"Mean $= {mean:.0f}$")
# Plot formatting
ax.set_xlabel("$X$ (sum of the two cards)")
ax.set_ylabel("$P(X)$")
ax.set_xticks(x_vals)
ax.set_xlim(2, 14)
ax.set_ylim(0, 0.4)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper right")

plt.tight_layout()
#If using termux
plt.savefig("figs/PMF.png")
#subprocess.run(shlex.split("termux-open figs/PMF.png"))
#else
plt.show()

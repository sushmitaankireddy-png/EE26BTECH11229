import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
import subprocess
import shlex

from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

cards = np.array([1, 3, 5, 7])

# Calculate theoretical PMF, mean, and variance
sums_anal = np.array([a + b for a, b in combinations(cards, 2)])
x_vals = np.unique(sums_anal)
panal = np.array([np.sum(sums_anal == x) / len(sums_anal) for x in x_vals])

mean_anal = np.sum(x_vals * panal)
var_anal = np.sum((x_vals**2) * panal) - mean_anal**2

# Run Monte Carlo simulation for card draws without replacement
simlen = 100000
sim_draws = np.array([np.random.choice(cards, size=2, replace=False) for _ in range(simlen)])
X_sim = np.sum(sim_draws, axis=1)

unique_sim, counts_sim = np.unique(X_sim, return_counts=True)
psim = counts_sim / simlen

mean_sim = np.mean(X_sim)
var_sim = np.var(X_sim)

print("X           :", x_vals)
print("P_anal(X)   :", np.round(panal, 4))
print("P_sim(X)    :", np.round(psim, 4))
print(f"Mean (Anal) = {mean_anal:.4f}  |  Mean (Sim) = {mean_sim:.4f}")
print(f"Var  (Anal) = {var_anal:.4f}  |  Var  (Sim) = {var_sim:.4f}")

# Plot theoretical stems and overlay simulation markers
fig, ax = plt.subplots(figsize=(8, 6))

pmf_pts = np.block([[x_vals], [panal]])
for i in range(len(x_vals)):
    A = np.array([x_vals[i], 0.0]).reshape(-1, 1)
    B = np.array([x_vals[i], panal[i]]).reshape(-1, 1)
    stem = line_gen(A, B)
    ax.plot(stem[0, :], stem[1, :], color="crimson", lw=2.5)

ax.plot(pmf_pts[0, :], pmf_pts[1, :], "o", color="darkred", markersize=7, zorder=5, label="Analysis")
label_pts(pmf_pts, ["1/6", "1/6", "2/6", "1/6", "1/6"])

ax.plot(unique_sim, psim, "o", color="C0", markersize=6, zorder=6, label="Simulation")

A_x = np.array([2.0, 0.0]).reshape(-1, 1)
B_x = np.array([14.0, 0.0]).reshape(-1, 1)
x_axis = line_gen(A_x, B_x)
ax.plot(x_axis[0, :], x_axis[1, :], color="black", lw=1)

A_m = np.array([mean_anal, 0.0]).reshape(-1, 1)
B_m = np.array([mean_anal, 0.4]).reshape(-1, 1)
m_line = line_gen(A_m, B_m)
ax.plot(m_line[0, :], m_line[1, :], color="blue", linestyle="--", lw=1.5, label=rf"Mean $= {mean_anal:.0f}$")

ax.set_xlabel("$X$ (sum of the two cards)")
ax.set_ylabel("$P(X)$")
ax.set_xticks(x_vals)
ax.set_xlim(2, 14)
ax.set_ylim(0, 0.4)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper right")

plt.tight_layout()

plt.savefig("figs/PMF.png")
# subprocess.run(shlex.split("termux-open figs/PMF.png"))
plt.show()

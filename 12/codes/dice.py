import numpy as np
import matplotlib.pyplot as plt

pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Joint PMF of (Y1, Y2)
joint_pmf = {(0, 0): 1/6, (0, 1): 1/3, (1, 0): 1/3, (1, 1): 1/6}
joint = [joint_pmf[p] for p in pairs]

# Individual PMFs of Y1 and Y2
p_Y1 = [1/2, 1/2]
p_Y2 = [1/2, 1/2]
prod = [p_Y1[a] * p_Y2[b] for (a, b) in pairs]

for p, j, q in zip(pairs, joint, prod):
    print(f"{p}: joint = {j:.4f}, product of individual PMFs = {q:.4f}")

# Grouped bar plot
x = np.arange(len(pairs))
w = 0.35

plt.figure()
plt.bar(x - w/2, joint, w, label="Joint PMF")
plt.bar(x + w/2, prod, w, label="Product of individual PMFs")
plt.xticks(x, [f"({a},{b})" for (a, b) in pairs])
plt.xlabel(r"$(Y_1, Y_2)$")
plt.ylabel("Probability")
plt.title("Die: joint PMF vs product of individual PMFs")
plt.legend()
plt.savefig("figs/dice.png", dpi=150, bbox_inches="tight")
plt.show()

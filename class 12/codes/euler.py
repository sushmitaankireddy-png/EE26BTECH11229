import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if
# Import custom modules
from CoordGeo.line.funcs import line_gen
from CoordGeo.plotting.funcs import label_pts

# Simulation parameters
h = 0.02
x0, y0 = 1.0, 0.0          # initial condition y(1) = 0
x_max = 1.4                # solution blows up near x ~ 1.43 (where y = x)
N = int(round((x_max - x0) / h))   # 20 steps -> 21 grid points

# Initialize arrays for numerical solution
x_num = x0 + h * np.arange(N + 1)
y_num = np.zeros(N + 1)
y_num[0] = y0

# Euler recurrence: y_{n+1} = y_n + h * (x_n + 2 y_n)/(x_n - y_n)
# Written with a column state vector [x_n, y_n]^T
for n in range(N):
    state = np.array([x_num[n], y_num[n]]).reshape(-1, 1)
    slope = (state[0, 0] + 2 * state[1, 0]) / (state[0, 0] - state[1, 0])
    y_num[n + 1] = y_num[n] + h * slope

# Numerical first derivative: y'_n = (y_{n+1} - y_n) / h
v_num = (y_num[1:] - y_num[:-1]) / h
x_der = x_num[:-1]

# Theoretical solution (parametric, v = y/x):
# ln x = -1/2 ln(v^2+v+1) + sqrt(3) atan((2v+1)/sqrt(3)) - C,  C = pi*sqrt(3)/6
C = np.pi * np.sqrt(3) / 6
v_par = np.linspace(0, 0.999, 5000)
x_par = np.exp(-0.5 * np.log(v_par**2 + v_par + 1)
               + np.sqrt(3) * np.arctan((2 * v_par + 1) / np.sqrt(3)) - C)
y_par = v_par * x_par
mask = x_par <= x_max
x_fine, y_exact = x_par[mask], y_par[mask]
v_exact = (x_fine + 2 * y_exact) / (x_fine - y_exact)   # y' from the ODE

# Target (initial) point x = 1, y = 0, y' = 1
x_target, y_target = 1.0, 0.0
v_target = (x_target + 2 * y_target) / (x_target - y_target)

# Define column vector target points for labeling
target_pt_y = np.array([x_target, y_target]).reshape(-1, 1)
target_pt_v = np.array([x_target, v_target]).reshape(-1, 1)

# Create stacked subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Top Subplot: y(x)
ax1.plot(x_fine, y_exact, 'b--', linewidth=2,
         label=r'Theoretical $y(x)$:' + '\n' +
               r'$\sqrt{3}\,\tan^{-1}\left(\frac{x+2y}{\sqrt{3}\,x}\right)-\frac{1}{2}\ln(x^2+xy+y^2)=\frac{\pi}{2\sqrt{3}}$')
ax1.stem(x_num, y_num, linefmt='r-', markerfmt='ro', basefmt='k-', label=r'Euler Recurrence ($y_n$)')
ax1.plot(target_pt_y[0, 0], target_pt_y[1, 0], 'go', markersize=8, label=r'Initial Point $(1,0)$')
label_pts(target_pt_y, [r'$(1,0)$'])

# Baseline axis generation using line_gen
x_base_top = line_gen(np.array([x0, 0]).reshape(-1, 1), np.array([x_max, 0]).reshape(-1, 1))
ax1.plot(x_base_top[0, :], x_base_top[1, :], 'k-', linewidth=0.5)

ax1.set_ylabel('$y(x)$')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left', fontsize=9)

# Bottom Subplot: y'(x)
ax2.plot(x_fine, v_exact, 'b--', label=r"Theoretical $y'(x)=\frac{x+2y}{x-y}$", linewidth=2)
ax2.stem(x_der, v_num, linefmt='r-', markerfmt='ro', basefmt='k-', label=r"Numerical Derivative ($y_n'$)")
ax2.plot(target_pt_v[0, 0], target_pt_v[1, 0], 'go', markersize=8, label=r'Initial Point $y^\prime(1)=1$')
label_pts(target_pt_v, [r"$y'(1)=1$"])

# Baseline axis generation using line_gen
x_base_bot = line_gen(np.array([x0, 0]).reshape(-1, 1), np.array([x_max, 0]).reshape(-1, 1))
ax2.plot(x_base_bot[0, :], x_base_bot[1, :], 'k-', linewidth=0.5)

ax2.set_xlabel('$x$')
ax2.set_ylabel(r"$y^\prime(x)$")
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left')

plt.tight_layout()
#If using termux
plt.savefig("figs/Euler.png")
#subprocess.run(shlex.split("termux-open Euler.png"))
#else
plt.show()

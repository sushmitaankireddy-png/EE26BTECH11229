import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if

# Import custom modules
from CoordGeo.plotting.funcs import label_pts

# Unit step function
def u(n):
    return np.heaviside(n, 1)

# A.Ps in terms of the unit step function, index starting from 0
# x1(n) = (63 + 2n) u(n), x2(n) = (3 + 7n) u(n)
def x1(n):
    return (63 + 2 * n) * u(n)

def x2(n):
    return (3 + 7 * n) * u(n)

# Intersection: 63 + 2n = 3 + 7n  =>  (2 - 7) n = 3 - 63
n0 = np.linalg.solve(np.array([[2.0 - 7.0]]), np.array([3.0 - 63.0]))[0]
n0 = int(round(n0))
print("n =", n0)
print("x1(n), x2(n) =", x1(n0), x2(n0))
print("Equal terms are the term number", n0 + 1)

# Stem plot
n = np.arange(-3, 16)

plt.stem(n - 0.1, x1(n), linefmt='b-', markerfmt='bo', basefmt='k-', label=r'$x_1(n) = (63 + 2n)u(n)$')
plt.stem(n + 0.1, x2(n), linefmt='g-', markerfmt='gs', basefmt='k-', label=r'$x_2(n) = (3 + 7n)u(n)$')

# Marking the stem where both sequences are equal
P = np.array([n0, x1(n0)]).reshape(-1, 1)
plt.plot([n0, n0], [0, x1(n0)], 'r-', linewidth=2)
plt.scatter(P[0, :], P[1, :], color='r', zorder=5)
label_pts(P, [f'({n0}, {int(x1(n0))})'])

plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.legend(loc='best')
plt.grid()

plt.tight_layout()
#If using termux
plt.savefig("figs/ap_equal.png")
#subprocess.run(shlex.split("termux-open figs/ap_equal.png"))
#else
plt.show()

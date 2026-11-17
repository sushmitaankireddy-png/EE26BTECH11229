import numpy as np
import matplotlib.pyplot as plt

#Given points
P = np.array([2,-2])
Q = np.array([3,7])
x = 24/11

#R - P = lambda (Q - P), from the first row
lam = (x - P[0])/(Q[0] - P[0])
R = P + lam*(Q - P)

#Verify that rank [Q-P R-P] = 1
print(np.linalg.matrix_rank(np.column_stack((Q-P, R-P))))
print("lambda =", lam, " y =", R[1], " ratio =", lam, ":", 1-lam)

#Plotting
pts = np.column_stack((P, Q, R))
plt.plot(pts[0,[0,1]], pts[1,[0,1]], 'C0-')
plt.scatter(pts[0], pts[1], color='C1', zorder=3)
plt.annotate('$\\mathbf{P}(2,-2)$', P, textcoords='offset points', xytext=(-45,-5))
plt.annotate('$\\mathbf{Q}(3,7)$', Q, textcoords='offset points', xytext=(5,0))
plt.annotate('$\\mathbf{R}\\left(\\frac{24}{11},-\\frac{4}{11}\\right)$', R, textcoords='offset points', xytext=(8,-12))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()

plt.savefig('figs/section.png')
plt.show()

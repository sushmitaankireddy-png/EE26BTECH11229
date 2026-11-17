import numpy as np
import matplotlib.pyplot as plt

#Roots of 2k^2 - 5k + 2 = 0
K = np.roots([2,-5,2])
print("k =", K)

#Points A, B, C for each k
def points(k):
	A = np.array([k+1, 2*k])
	B = np.array([3*k, 2*k+3])
	C = np.array([5*k-1, 5*k])
	return A, B, C

#Plotting
for i, k in enumerate(sorted(K)):
	A, B, C = points(k)
	#Verify that rank [B-A C-A] = 1
	print(k, np.linalg.matrix_rank(np.column_stack((B-A, C-A))))
	pts = np.column_stack((A, B, C))
	order = np.lexsort((pts[1], pts[0]))
	plt.plot(pts[0,order], pts[1,order], 'C%d-' % i, label='$k = %.1f$' % k)
	plt.scatter(pts[0], pts[1], color='C%d' % i, zorder=3)
	for name, p in zip('ABC', (A, B, C)):
		plt.annotate('$\\mathbf{%s}$' % name, p, textcoords='offset points', xytext=(6,6))

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.axis('equal')
plt.grid()

plt.savefig('figs/collinear.png')
plt.show()

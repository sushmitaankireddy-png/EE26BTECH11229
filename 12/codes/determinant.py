import numpy as np

# Given A(adj A) = 8I
M = np.array([[8, 0],
              [0, 8]])

# Formula: A(adj A) = det(A) * I
I = np.eye(2)

det_A = M[0, 0]

# Verify the determinant formula
if np.allclose(M, det_A * I):
    print("Determinant |A| =", int(det_A))
else:
    print("Invalid matrix equation")

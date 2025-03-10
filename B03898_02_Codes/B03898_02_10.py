""""
README
======
This file contains Python codes.
======
"""

""" Solve Ax=B with the Jacobi method """
import numpy as np

def jacobi(A, B, n, tol=1e-10):
    # Initializes x with zeroes with same shape and type as B
    x = np.zeros_like(B)

    for it_count in range(n):
        x_new = np.zeros_like(x)        
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (B[i] - s1 - s2) / A[i, i]

        if np.allclose(x, x_new, tol):
            break

        x = x_new

    return x

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
B = np.array([6., 25., -11., 15.])
n = 25

x = jacobi(A,B,n)
print ("x =", x)


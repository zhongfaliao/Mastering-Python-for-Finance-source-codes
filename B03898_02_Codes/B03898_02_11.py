""""
README
======
This file contains Python codes.
======
"""

""" Solve Ax=B with the Gauss-Seidel method """
import numpy as np


def gauss(A, B, n, tol=1e-10):
    L = np.tril(A)  # Returns the lower triangular matrix of A
    U = A - L  # Decompose A = L + U
    L_inv = np.linalg.inv(L)
    x = np.zeros_like(B)
    
    for i in range(n):        
        Ux = np.dot(U, x)
        x_new = np.dot(L_inv, B - Ux)
        
        if np.allclose(x, x_new, tol):
            break
            
        x = x_new
        
    return x

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
B = np.array([6., 25., -11., 15.])
n = 100
x = gauss(A, B, n)
print ("x =", x)




""""
README
======
This file contains Python codes.
======
"""

""" LU decomposition with SciPy """
import scipy.linalg as linalg
import numpy as np

A = np.array([[2., 1., 1.],
              [1., 3., 2.],
              [1., 0., 0.]])
B = np.array([4., 5., 6.])

LU = linalg.lu_factor(A)
x = linalg.lu_solve(LU, B)

print (x)

P, L, U = linalg.lu(A)
print (P)
print (L)
print (U)


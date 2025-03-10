""""
README
======
This file contains Python codes.
======
"""

""" Cholesky decomposition with NumPy """
import numpy as np

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
B = np.array([6., 25., -11., 15.])

L = np.linalg.cholesky(A)

print(L)

print(np.dot(L, L.T.conj()) ) # A=L.L*)


y = np.linalg.solve(L, B)  # L.L*.x=B. When L*.x=y, then L.y=B.
print(y)

x = np.linalg.solve(L.T.conj(), y)  # x=L*'.y
print(x)

print(np.mat(A) * np.mat(x).T ) # B=Ax)


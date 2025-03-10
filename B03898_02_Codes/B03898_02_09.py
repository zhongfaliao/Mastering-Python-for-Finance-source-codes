""""
README
======
This file contains Python codes.
======
"""

""" QR decomposition with scipy """
import scipy
import numpy as np

A = np.array([
    [2., 1., 1.],
    [1., 3., 2.],
    [1., 0., 0]])
B = np.array([4., 5., 6.])

Q, R = scipy.linalg.qr(A)  # QR decomposition
y = np.dot(Q.T, B)  # Let y=Q'.B
x = scipy.linalg.solve(R, y)  # Solve Rx=y
print(x)

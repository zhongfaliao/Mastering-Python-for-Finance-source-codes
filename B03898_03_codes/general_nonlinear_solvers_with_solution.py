""""
README
======
This file contains Python codes.
======
"""

"""
General nonlinear solvers
- with a solution
"""


import scipy.optimize as optimize

y = lambda x: x**3 + 2.*x**2 - 5.
dy = lambda x: 3.*x**2 + 4.*x

print (optimize.fsolve(y, 5., fprime=dy))
print (optimize.root(y, 5.))

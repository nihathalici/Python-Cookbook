# Exer-10-Performing-Matrix-and-Linear-Algebra-Calculations.py

import numpy as np

m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])

print(m)
print(m.T)
print(m.I)

v = np.matrix([[2],[3],[4]])
print(v)
print(m*v)

import numpy.linalg

print(numpy.linalg.det(m))

print(numpy.linalg.eigvals(m))
x = numpy.linalg.solve(m, v)
print(x)
print(m*x)
print(v)

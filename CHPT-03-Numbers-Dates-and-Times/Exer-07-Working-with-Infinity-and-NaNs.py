# Exer-07-Working-with-Infinity-and-NaNs.py

a = float('inf')
b = float('-inf')
c = float('nan')

print(a)
print(b)
print(c)

import math

print(math.isinf(a))
print(math.isnan(c))

print(a + 45)
print(a * 10)
print(10 / a)

print(a / a)
print(a + b)

print(c + 23)
print(c / 2)
print(c * 2)
print(math.sqrt(c))

c = float('nan')
d = float('nan')
print(c == d)
print(c is d)
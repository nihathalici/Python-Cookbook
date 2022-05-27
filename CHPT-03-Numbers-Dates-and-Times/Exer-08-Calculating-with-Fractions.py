# Exer-08-Calculating-with-Fractions.py

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

c = a * b

print(c.numerator)
print(c.denominator)

print(float(c))

print(c.limit_denominator(8))

x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
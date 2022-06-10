# Exer-12-Iterating-on-Items-in-Separate-Containers

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

###

active_items = set()
inactive_items = set()

for item in chain(active_items, inactive_items):
    ...

for item in active_items:
    ...

for item in inactive_items:
    ...

for x in a + b:  # Inefficient

for x in chain(a, b):  # Better

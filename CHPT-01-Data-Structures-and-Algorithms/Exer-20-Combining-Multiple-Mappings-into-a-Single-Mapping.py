# Exer-20-Combining-Multiple-Mappings-into-a-Single-Mapping.py

from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a, b)

print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))

print(list(c.keys()))

print(list(c.values()))

c['z'] = 10

c['w'] = 40

del c['x']

print(a)

del c['y'] # Error!

values = ChainMap()
values['x'] = 1

print(values)

values = values.new_child()
values['x'] = 2

values = values.new_child()
values['x'] = 3

values = values.parents
values['x']
print(values['x'])

values = values.parents
values['x']
print(values['x'])
print(values)

###

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

a['x'] = 13
print(merged['x'])

###

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = ChainMap(a, b)
print(merged['x'])

a['x'] = 42
print(merged['x'])

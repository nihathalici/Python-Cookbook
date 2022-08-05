# Exer-14-Implementing-Custom-Containers

import collections

class A(collections.Iterable):
    pass

# a = A()  # TypeError: Can't instantiate abstract class A with abstract methods __iter__

# collections.Sequence()  # TypeError: Can't instantiate abstract class Sequence

import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)
    
items = SortedItems([5, 1, 3])
list(items)
print(items[0])
print(items[-1])
items.add(2)
items.add(-10)
items[1:4]
3 in items
len(items)
for n items:
    print(n)

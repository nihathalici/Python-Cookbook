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

###

items = SortedItems()
import collections

isinstance(items, collections.Iterable)
isinstance(items, collections.Sequence)
isinstance(items, collections.Container)
isinstance(items, collections.Sized)
isinstance(items, collections.Mapping)

###

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)

a = Items([1, 2, 3])
len(a)
a.append(4)
a.append(2)
a.remove(3)        

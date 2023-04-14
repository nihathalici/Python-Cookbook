# Exer-14-Making-Your-Programs-Run-Faster

# somescript.py

import sys
import csv

with open(sys.srgv[1]) as f:
    for row in csv.reader(f):
        # Some kind of processing
        ...

###

import sys
import csv

def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
            # Some kind of processing
            # ...

main(sys.argv[1])

###

import math

def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

# Test
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)

###

###
# faster version

from math import sqrt

def compute_roots(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

# Test
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)

###

import math

def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

###

# Slower

class SomeClass:
    ...
    def method(self):
        for x in s:
            op(self.value)

# Faster

class SomeClass:
    ...
    def method(self):
        value = self.value
        for x in s:
            op(value)

###

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

from timeit import timeit
a = A(1, 2)
timeit('a.x', 'from __main__ import a')
timeit('a.y', 'from __main__ import a')

###

values = [x for x in sequence]
squares = [x*x for x values]
squares = [x*x for x sequence]

###

a = {
    'name' : 'AAPL',
    'shares' : 100,
    'price' : 534.22
}

b = dict(name="AAPL", shares=100, price=534.22)
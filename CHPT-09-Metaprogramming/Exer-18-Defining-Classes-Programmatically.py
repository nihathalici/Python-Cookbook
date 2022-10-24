# Exer-18-Defining-Classes-Programmatically

def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

import collections
import types
from unicodedata import name

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

s = Stock('ACME', 50, 91.1)
print(s.cost())

###

import abc

Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
print(Stock)
print(type(Stock))

class Spam(Base, debug=True, typecheck=False)
...

Spam = types.new_class('Spam', (Base,), 
                       {'debug': True, 'typecheck': False},
                       lambda ns: ns.update(cls_dict)) 

###

Stock = collections.namedtuple('Stock', ['name', 'shares', 'price'])

###

import operator
import types
import sys

def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = { name: property(operator.itemgetter(n))
                 for n, name in enumerate(fieldnames) }
    
    # Make a __new__ function and add to the class dict
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)
    
    cls_dict['__new__'] = __new__

    # Make the class
    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))

    # Set the module to that of the caller
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls

###

Point = named_tuple('Point', ['x', 'y'])
p = Point(4, 5)
len(p)
p.x
p.y
p.x = 2  # AttributeError: can't set attribute
print('%s %s' % p)

Stock = type('Stock', (), cls_dict)

###

import types

metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})
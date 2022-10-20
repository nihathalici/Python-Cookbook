# Exer-16-Enforcing-an-Argument-Signature-on-args-and-kwargs

from inspect import Signature, Parameter

# Make a signature for a func(x, y = 42, *, z = None)
parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(parms)
#print(sig)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)

# Try various examples
#print(func(1, 2, z=3))
#print(func(1))
#print(func(1, z=3))
#print(func(y=2, x=1))
# print(func(1, 2, 3, 4))  # TypeError: too many positional arguments
# print(func(y=2))  # TypeError: 'x' parameter lacking default value
# print(func(1, y=2, x=3))  # TypeError: multiple values for argument 'x'

###

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# Example use
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')

class Point(Structure):
    __signature__ = make_sig('x', 'y')


import inspect

#print(inspect.signature(Stock))
#s1 = Stock('ACME', 100, 490.1)
#s2 = Stock('ACME', 100)  # TypeError: multiple values for argument 'shares'

###

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value) 

# Example
class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

###

import inspect
print(inspect.signature(Stock))
print(inspect.signature(Point))



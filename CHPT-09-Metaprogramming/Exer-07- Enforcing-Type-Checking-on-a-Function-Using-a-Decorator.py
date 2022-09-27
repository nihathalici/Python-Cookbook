# Exer-07- Enforcing-Type-Checking-on-a-Function-Using-a-Decorator
"""
@typeassert(int, int)
def add(x, y):
    return x + y

print(add(2, 3))
print(add(2, 'hello'))  # TypeError
"""

from inspect import signature 
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func
        
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate
        
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

print(spam(1, 2, 3))
print(spam(1, "hello", 3))
print(spam(1, 'hello', 'world'))  # TypeError

###

from inspect import signature

def spam(x, y, z=42):
    pass

sig = signature(spam)
print(sig)
sig.parameters
sig.parameters['z'].name
sig.parameters['z'].default
sig.parameters['z'].kind

###

bound_types = sig.bind_partial(int, z=int)
bound_types
bound_types.arguments

###

bound_values = sig.bind(1, 2, 3)
bound_values.arguments

for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError()

@typeassert
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

bar(2)
bar(2, 3) # TypeError
bar(4, [1, 2, 3])

@typeassert
def spam(x:int, y, z:int = 42):
    print(x, y, z)


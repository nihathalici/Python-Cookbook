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



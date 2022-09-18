# Exer-02-Preserving-Function-Metadata-When-Writing-Decorators

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

print(countdown(100000))
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

print(countdown.__wrapped__(100000))

###

from inspect import signature

print(signature(countdown))
# Exer-01-Putting-a-Wrapper-Around-a-Function

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
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1

print(countdown(100000))
print(countdown(10000000))

###

class A:
    @classmethod
    def method(cls):
        pass

class B:
    def method(cls):
        pass
    method = classmethod(method)

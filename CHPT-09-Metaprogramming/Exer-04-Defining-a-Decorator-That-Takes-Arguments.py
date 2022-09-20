# Exer-04-Defining-a-Decorator-That-Takes-Arguments

from functools import wraps
import logging
from symbol import decorator

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


@decorator(x, y, z)
def func(a, b):
    pass

def func(a, b):
    pass

func = decorator(x, y, z)(func)




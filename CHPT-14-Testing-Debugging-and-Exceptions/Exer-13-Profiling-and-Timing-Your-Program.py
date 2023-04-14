# Exer-13-Profiling-and-Timing-Your-Program

# using Unix time command
# bash % time python3 someprogram.py

# using cProfile module
# bash % python3 -m cProfile someprogram.py

# timethis.py

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print("{}.{} : {}".format(func.__module__, func.__name__, end - start))
        return r

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000000)

###

from contextlib import contextmanager


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print("{} : {}".format(label, end - start))


with timeblock("counting"):
    n = 10000000
    while n > 0:
        n -= 1

###

from timeit import timeit

timeit("math.sqrt(2)", "import math")

timeit("sqrt(2)", "from math import sqrt")

###

timeit("math.sqrt(2)", "import math", number=10000000)

timeit("sqrt(2)", "from math import sqrt", number=10000000)

###

# Using time.process_time() function

from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print("{}.{} : {}".format(func.__module__, func.__name__, end - start))
        return r

    return wrapper

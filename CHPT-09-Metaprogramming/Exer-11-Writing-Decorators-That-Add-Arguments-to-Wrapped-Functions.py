# Exer-11-Writing-Decorators-That-Add-Arguments-to-Wrapped-Functions

from functools import wraps 

def optional_debug(func):
    @wraps(func)
    def wrappper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrappper

@optional_debug
def spam(a, b, c):
    print(a, b, c)

spam(1, 2, 3)
spam(1, 2, 3, debug=True)
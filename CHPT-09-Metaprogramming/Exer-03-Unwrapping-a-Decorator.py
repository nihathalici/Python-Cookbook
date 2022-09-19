# Exer-03-Unwrapping-a-Decorator
'''
@somedecorator
def add(x, y):
    return x + y

orig_add = add.__wrapped__
orig_add(3, 4)
'''

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

print(add(2, 3))
print(add.__wrapped__(2, 3))



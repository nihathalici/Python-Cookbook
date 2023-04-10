# Exer-09-Raising-an-Exception-in-Response-to-Another-Exception

def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e...

example()  # RuntimeError => ValueError

###

try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)

###

def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse:", err)

example2()  # ValueError => NameError

###

def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None...

example3()  # RuntimeError

###

"""
try:
    ...
except SomeException as e:
    raise DifferentException() from e

###
    
try:
    ...
except SomeException:
    raise DifferentException()
"""
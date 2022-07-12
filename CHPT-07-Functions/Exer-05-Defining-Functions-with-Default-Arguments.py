# Exer-05-Defining-Functions-with-Default-Arguments

def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)

# Using a list as a default value
def spam(a, b=None):
    if b is None:
        b = []

_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

spam(1)
print(spam(1, 2))
print(spam(1, None))



x = 42
def spam(a, b=x):
    print(a, b)
spam(1)

x = 23  # Has no effect
spam(1)

###

def spam(a, b=[]):  # NO!!!
    print(b)
    return b

x = spam(1)
print(x)

x.append(99)
x.append('Yow!')
print(x)
spam(1)  # Modified list gets returned!


###

def spam(a, b=None):
    if not b:  # NO! Use 'b is None' instead
        b = []

print(spam(1))
x = []

print(spam(1, x))  # Silent error. x value overwritten by default
print(spam(1, 0))  # Silent error. 0 ignored
print(spam(1, ''))  # Silent error. '' ignored

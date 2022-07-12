# Exer-06-Defining-Anonymous-or-Inline-Functions

add = lambda x, y: x + y
print( add(2, 3) )
print( add('hello', 'world') )

###

def add(x, y):
    return x + y

print( add(2, 3) )

###

names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']

print( sorted(names, key=lambda name: name.split()[-1].lower()) )

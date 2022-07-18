# Exer-01-Changing-the-String-Representation-of Instances

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3,4)
p  # __repr__() output
print(p)  # __str__() output

print('p is {0!r}'.format(p))  # output: p is Pair(3, 4)

print('p is {0}'.format(p))  # output: p is (3, 4)

f = open('file.dat')
f

def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)

def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)

        

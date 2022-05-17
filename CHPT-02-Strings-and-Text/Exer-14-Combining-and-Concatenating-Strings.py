# Exer-14-Combining-and-Concatenating-Strings.py

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print( ' '.join(parts) )

print( ','.join(parts)  )

print( ''.join(parts) )  

###

a = 'Is Chicago'
b = 'Not Chicago?'

print(a + ' ' + b)

###

print('{} {}'.format(a, b))
print( a + ' ' + b )

###

a = 'Hello' 'World'
print(a)

###

s = ''
for p in parts:
    s += p

print(s)

###

data = ['ACME', 50, 91.1]

print( ','.join( str(d) for d in data ) )

###

# print( a + ':' + b + ':' + c )  # Ugly
# print(':'.join([a, b, c]))      # Still Ugly
# print(a, b, c, sep=':')         # Better

###

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())
print(text)

for part in sample():
    f.write(part) 

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    f.write(part)
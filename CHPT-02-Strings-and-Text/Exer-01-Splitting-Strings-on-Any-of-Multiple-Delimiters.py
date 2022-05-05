# Exer-01-Splitting-Strings-on-Any-of-Multiple-Delimiters.py

import re

line = 'asdf fjdk; afed, fjek,asdf,     foo'
print(re.split(r'[;,\s]\s*', line))

###

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

###

values = fields[::2]
delimiters = fields[1::2] + ['']

print(values)
print(delimiters)

###

print(''.join( v+d for v,d in zip(values, delimiters)))

###

print( re.split(r'(?:,|;|\s)\s*', line) )

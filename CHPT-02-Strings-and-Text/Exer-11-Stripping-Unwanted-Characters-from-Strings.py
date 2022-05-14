# Exer-11-Stripping-Unwanted-Characters-from-Strings.py

s = '   hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

###

t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

###

s = ' hello   world \n'
s = s.strip()
print(s)
print(s.replace(' ', ''))

###

import re

print( re.sub('\s+', ' ', s) )

###

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:

        

# Exer-04-Working-with-Binary-Octal-and-Hexadecimal-Integers.py

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print( format(x, 'b') )
print( format(x, 'o') )
print( format(x, 'x') )

###

x = -1234
print( format(x, 'b') )
print( format(x, 'x') )

print( format(2**32 + x, 'b') )
print( format(2**32 + x, 'x') )

###

print( int('4d2', 16) )
print( int('10011010010', 2) )

###

import os

# os.chmod('script.py', 0755) # SyntaxError: invalid token
# os.chmod('script.py', 0o755) # prefix the octal value to fix it

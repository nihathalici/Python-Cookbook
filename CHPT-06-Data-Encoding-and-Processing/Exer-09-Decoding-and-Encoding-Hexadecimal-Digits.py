# Exer-09-Decoding-and-Encoding-Hexadecimal-Digits

s = b'hello'

import binascii
h = binascii.b2a_hex(s)
print(h)

print(binascii.a2b_hex(h))

import base64

h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))

h = base64.b16encode(s)
print(h)
print(h.decode('ascii'))


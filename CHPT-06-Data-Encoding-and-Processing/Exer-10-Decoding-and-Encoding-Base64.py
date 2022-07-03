# Exer-10-Decoding-and-Encoding-Base64

s = b'hello'

import base64

a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))

a = base64.b64encode(s).decode('ascii')
print(a)

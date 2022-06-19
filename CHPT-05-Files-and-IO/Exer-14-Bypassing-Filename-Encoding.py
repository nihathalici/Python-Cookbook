# Exer-14-Bypassing-Filename-Encoding

import sys
print(sys.getfilesystemencoding())

###

# Wrte a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')

print('###')

# Directory listing (decoded)
import os
print(os.listdir('.'))

print('###')

# Directory listing (raw)
print(os.listdir(b'.'))

print('###')

# Open file with raw filename
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())




# Exer-17-Writing-Bytes-to-a-Text-File

import sys

print(sys.stdout.write(b'Hello\n')) # TypeError

print(sys.stdout.buffer.write(b'Hello\n'))  #AttributeError

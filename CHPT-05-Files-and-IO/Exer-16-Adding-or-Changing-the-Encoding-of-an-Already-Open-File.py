# Exer-16-Adding-or-Changing-the-Encoding-of-an-Already-Open-File

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

###

import sys
print(sys.stdout.encoding)
print('####')
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
#print(sys.stdout.encoding)
print('####')
f = open('somefile.txt', 'w')
print(f)
print(f.buffer)
print(f.buffer.raw)
print('####')
f = io.TextIOWrapper(f.buffer, encoding='latin-1')
f.write('Hello')
print('####')
f = io.TextIOWrapper(b, encoding='latin-1')
print('####')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')


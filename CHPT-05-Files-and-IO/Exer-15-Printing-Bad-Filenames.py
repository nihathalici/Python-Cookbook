# Exer-15-Printing-Bad-Filenames

def bad_filename(filename):
    return repr(filename)[1:-1]

try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))

###

import os

files = os.listdir('.')
files

for name in files:
    print(name)

###

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

###

def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))

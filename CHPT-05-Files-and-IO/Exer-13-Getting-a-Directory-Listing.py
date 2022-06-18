# Exer-13-Getting-a-Directory-Listing

import os

names = os.listdir('test')
print(names)

import os.path

# Get all regular files
names = [name for name in os.listdir('test')
         if os.path.isfile(os.path.join('test', name))]

print(names)

# Get all dirs
dirnames = [name for name in os.listdir('test')
            if os.path.isdir(os.path.join('test', name))]

print(dirnames)

pyfiles = [name for name in os.listdir('test')
           if name.endswith('.py')]

print(pyfiles)

print('###')

import glob
pyfiles = glob.glob('test/*.py')
print(pyfiles)

print('###')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('test')
           if fnmatch(name, '*.py')]
print(pyfiles)

print('###')

pyfiles = glob.glob('*.py')
print(pyfiles)

print('###')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

print('###')

# Alternative: Get file metadata

file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
                                

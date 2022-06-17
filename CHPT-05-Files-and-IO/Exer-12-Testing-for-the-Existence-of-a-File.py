# Exer-12-Testing-for-the-Existence-of-a-File

import os
print( os.path.exists('somefile.txt') )

print( os.path.isfile('somefile.txt') )

print( os.path.isdir('somefile.txt') )

print( os.path.islink('somefile.txt') )

print( os.path.realpath('somefile.txt') )

print( os.path.getsize('somefile.txt') )

print( os.path.getmtime('somefile.txt') )

import time

print( time.ctime(os.path.getmtime('somefile.txt')) )


# Exer-11-Manipulating-Pathnames

import os
# path = '/Users/beazley/Data/data.csv'

print( os.path.basename(path) )

print( os.path.dirname(path) )

print( os.path.join('tmp', 'data', os.path.basename(path) ) )

path = '~/Data/data.csv'
print(os.path.expanduser(path) )
print( os.path.splitext(path) )

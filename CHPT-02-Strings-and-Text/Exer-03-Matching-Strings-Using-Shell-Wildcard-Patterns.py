# Exer-03-Matching-Strings-Using-Shell-Wildcard-Patterns.py

from fnmatch import fnmatch, fnmatchcase

print( fnmatch('foo.txt', '*.txt') )

print( fnmatch('foo.txt', '?oo.txt') )

print( fnmatch('Dat45.csv', 'Dat[0-9]*') )

###

names = [ 'Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py' ]

print(  [ name for name in names if fnmatch(name, 'Dat*.csv') ]   )

# fnmatch('foo.txt', '*.TXT') # On OS X (Mac), False 
# fnmatch('foo.txt', '*.TXT') # On Windows, True

#print( fnmatchcase('foo.txt', '*.TXT') ) # False

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print( [addr for addr in addresses if fnmatchcase(addr, '* ST')]   )



# Exer-07-Reading-and-Writing-Compressed-Datafiles

# read
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# write
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# compression level
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

###

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

# Exer-11-Reading-and-Writing-Binary-Arrays-of-Structures

from struct import Struct

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

###

from struct import Struct

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            # Process rec

###

from struct import Struct

def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))

if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        # Process rec

###

record_struct = Struct('<idd')

###

from struct import Struct
record_struct = Struct('<idd')
print(record_struct.size)
print(record_struct.pack(1, 2.0, 3.0))
#print(record_struct.unpack(_))

###

import struct
print(struct.pack('<idd', 1, 2.0, 3.0))
#print(struct.unpack('<idd', _))

###

f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
chunks
for chk in chunks:
    print(chk)

###

def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records

###

def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))

###

from collections import namedtuple

Record = namedtuple('Record', ['kind', 'x', 'y'])

with open('data.p', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

for r in records:
    print(r.kind, r.x, r.y)

import numpy as np
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i, <d, <d')
print(records)
records[0]
records[1]

# Exer-19-Making-Temporary-Files-and-Directories

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()

###

f = TemporaryFile('w+t')
f.close()

###

with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:

###

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

###

with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

###

from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

###

import tempfile

print(tempfile.mkstemp())
print(tempfile.mkdtemp())

print(tempfile.gettempdir())

###
from tempfile import NamedTemporaryFile

f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
print(f.name)

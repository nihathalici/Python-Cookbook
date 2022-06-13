# Exer-05-Writing-to-a-File-That-Doesnt-Already-Exist


with open('somefile', 'wt') as f:
    f.write('Hello\n')

''' x mode is a Python 3 specific extension to open() func '''
with open('somefile', 'xt') as f:
    f.write('Hello\n')  # FileExistsError

###

import os

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')


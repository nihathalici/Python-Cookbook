# Exer-07-Copying-or-Moving-Files-and-Directories

import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)

###

shutil.copy2(src, dst, follow_symlinks=False)

shutil.copytree(src, dst, symlinks=True)

###

def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)

###

shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))

###

filename = '/Users/guido/programs/spam.py'

import os.path

os.path.basename(filename)
os.path.dirname(filename)
os.path.split(filename)
os.path.join('/new/dir', os.path.basename(filename))
os.path.expanduser('~/guido/programs/spam.py')

###

try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        print(dst, src, msg)

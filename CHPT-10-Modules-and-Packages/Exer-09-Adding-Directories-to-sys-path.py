# Exer-09-Adding-Directories-to-sys-path

"""
bash % env PYTHONPATH=/some/dir:/other/dir python3
"""

import sys
sys.path

"""
# myapplication.pth
/some/dir
/other/dir
"""

###

import sys
sys.path.insert(0, '/some/dir')
sys.path.insert(0, '/other/dir')

###

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, abspath(dirname('__file__'), 'src'))
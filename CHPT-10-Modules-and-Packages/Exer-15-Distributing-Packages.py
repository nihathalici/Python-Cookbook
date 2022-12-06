# Exer-15-Distributing-Packages

"""
projectname/
  README.txt
  Doc/
    documentation.txt
  projectname/
    __init__.py
    foo.oy
    bar.py
    utils/
      __init__.py
      spam.py
      grok.py
  examples/
    helloworld.py
    ...
"""

# setup.py
from distutils.core import setup

setup(name='projectname',
      version='1.0',
      author='Your Name',
      author_email='you@youraddress.com',
      url='http://www.you.com/projectname',
      packages=['projectname', 'projectname.utils'],
)

"""
# MANIFEST.in
include *.txt
recursive-include examples *
recursive-include Doc *
"""

"""
% bash python3 setup.py sdist 
"""

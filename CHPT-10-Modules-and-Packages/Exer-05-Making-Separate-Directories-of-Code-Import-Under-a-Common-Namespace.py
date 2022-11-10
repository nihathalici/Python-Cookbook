# Exer-05-Making-Separate-Directories-of-Code-Import-Under-a-Common-Namespace

"""
foo-package/
  spam/
    blah.py

bar-package/
  spam/
    grok.py
"""

import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok

###

import spam
spam.__path__

###

"""
my-package/
  spam/
    custom.py
"""

import spam.custom
import spam.grok
import spam.blah

spam.__file__ # AttributeError: 'module' object has no attribute '__file__'

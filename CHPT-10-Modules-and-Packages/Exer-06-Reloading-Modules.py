# Exer-06-Reloading-Modules
"""
import spam
import imp
imp.reload(spam)
"""

"""
# spam.py

def bar():
    print("bar")

def grok():
    print("grok")

import spam

from spam import grok

spam.bar()
#bar

grok()
#grok

def grok():
    print("New grok")

import imp
imp.reload(spam)

spam.bar()
#bar

grok()
# grok

spam.grok()  # New output
# New grok 
"""
# Exer-02-Controlling-the-Import-of-Everything

# somemodule.py

def spam():
    pass

def grok():
    pass

blah = 42

# Only export 'spam' and 'grok'
__all __ = ['spam', 'grok']


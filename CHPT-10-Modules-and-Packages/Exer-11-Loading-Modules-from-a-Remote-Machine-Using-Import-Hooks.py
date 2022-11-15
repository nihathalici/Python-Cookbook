# Exer-11-Loading-Modules-from-a-Remote-Machine-Using-Import-Hooks

'''
testcode/
  spam.py
  fib.py
  grok/
    __init__.py
    blah.py
'''

# spam.py
print(" I'm spam ")

def hello(name):
    print('Hello %s' % name)

# fib.py
print(" I'm fib ")

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# grok/__init__.py
print(" I'm grok.__init__ ")

# grok/blah.py
print("I'm grok.blah")

"""
bash % cd testcode
bash % python3 -m http.server 15000
Serving HTTP on 0.0.0.0 port 15000 
"""

from urllib.request import urlopen
u = urlopen('http://localhost:15000/fib.py')
data = u.read().decode('utf-8')
print(data)

###

# fib.py
print("I'm fib")

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

###

import imp
import urllib.request
import sys

def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod

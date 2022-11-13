# Exer-08-Reading-Datafiles-Within-a-Package

"""
mypackage/
  __init__.py
  somedata.dat
  spam.py
"""

# spam.py

import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
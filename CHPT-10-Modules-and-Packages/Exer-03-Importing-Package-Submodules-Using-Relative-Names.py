# Exer-03-Importing-Package-Submodules-Using-Relative-Names

"""
mypackage/
  __init__.py
  A/
    __init__.py
    spam.py
    grok.py
  B/
    __init__.py
    bar.py
"""

# mypackage/A/spam.py

from . import grok

###

# mypackage/A/spam.py

from ..B import bar

###

# mypackage/A/spam.py

from mypackage.A import grok # OK
from . import grok # OK
import grok     # Error (not found)

###

from . import grok  # OK
import . grok  # ERROR

###

# % python3 mypackage/A/spam.py # Relative imports fail

# % python3 -m mypackage/A/spam  # Relative imports work
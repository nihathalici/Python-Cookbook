# Exer-11-Issuing-Warning-Messages

import warnings


def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn("logfile argument deprecated", DeprecationWarning)
    ...


# -W error option
# bash % python3 -W error example.py

###

import warnings

warnings.simplefilter("always")
f = open("/etc/passwd")
del f  # ResourceWarning

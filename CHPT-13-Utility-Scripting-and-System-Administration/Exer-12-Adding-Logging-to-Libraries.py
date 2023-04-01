# Exer-12-Adding-Logging-to-Libraries

# somelib.py

import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Example function (for testing)
def func():
    log.critical("A Critical Error!")
    log.debug("A debug message")


###

import logging

logging.basicConfig()
somelib.func()

###

import logging

logging.basicConfig(level=logging.ERROR)
import somelib

somelib.func()

###

# Change the logging level for 'somelib' only
logging.getLogger("somelib").level = logging.DEBUG
somelib.func()

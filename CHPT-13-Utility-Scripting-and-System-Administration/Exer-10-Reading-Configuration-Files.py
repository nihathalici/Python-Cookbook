# Exer-10-Reading-Configuration-Files

from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("config.ini")
cfg.sections()
cfg.get("installation", "library")
cfg.getboolean("debug", "log_errors")
cfg.getint("server", "port")
cfg.getint("server", "nworkers")
print(cfg.get("server", "signature"))

###

cfg.set("server", "port", "9000")
cfg.set("debug", "log_errors", "False")

import sys

cfg.write(sys.stdout)
cfg.get("installation", "PREFIX")
cfg.get("installation", "prefix")

###

# Previously read configuration
cfg.get("installation", "prefix")

# Merge in user-specific configuration
import os

cfg.read(os.path.expanduser("~/.config.ini"))
cfg.get("installation", "prefix")
cfg.get("installation", "library")
cfg.getboolean("debug", "log_errors")

###

cfg.get("installation", "library")

cfg.set("installation", "prefix", "/tmp/dir")

cfg.get("installation", "library")

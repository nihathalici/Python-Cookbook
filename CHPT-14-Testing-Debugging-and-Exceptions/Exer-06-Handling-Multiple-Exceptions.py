# Exer-06-Handling-Multiple-Exceptions

"""
try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)

###
    
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url(url)
except SocketTimeout:
    client_obj.handle_url_timeout(url)

###

try:
    f = open(filename)
except (FileNotFoundError, PermissionError):
    ...
"""

try:
    f = open(filename)
except OSError:
    ...

try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error("File not found")
    elif e.errno == errno.EACCES:
        logger.error("Permission denied")
    else:
        logger.error("Unexpected error: %d", e.errno)

###

f = open("missing")  # FileNotFoundError: [Errno 2] No such file or directory: 'missing'

###

try:
    f = open("missing")
except OSError:
    print("It failed")
except FileNotFoundError:
    print("File not found")

# Prints: It failed

###

FileNotFoundError.__mro__

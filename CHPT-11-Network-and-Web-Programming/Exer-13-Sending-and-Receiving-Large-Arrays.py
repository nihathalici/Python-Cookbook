# Exer-13-Sending-and-Receiving-Large-Arrays

# zerocopy.py
def send_from(arr, dest):
    view = memoryview(arr).cast("B")
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]


def recv_into(arr, source):
    view = memoryview(arr).cast("B")
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]


from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 25000))
s.listen(1)
c, a = s.accept()

###

from socket import *

c = socket(AF_INET, SOCK_STREAM)
c.connect(("localhost", 25000))

###

# Server
import numpy

a = numpy.arange(0.0, 50000000.0)
send_from(a, c)

# Client
a = numpy.zeros(shape=50000000, dtype=float)
a[0:10]
recv_into(a, c)
a[0:10]

view = memoryview(arr).cast("B")

# Exer-11-Passing-a-Socket-File-Descriptor-Between-Processes

import multiprocessing
from multiprocessing.reduction import recv_handle, send_handle
import socket


def worker(in_p, out_p):
    out_p.close()
    while True:
        fd = recv_handle(in_p)
        print("CHILD: GOT FD", fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as s:
            while True:
                msg = s.recv(1024)
                if not msg:
                    break
                print("CHILD: RECV {!r}".format(msg))
                s.send(msg)


def server(address, in_p, out_p, worker_pid):
    in_p.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(address)
    s.listen(1)
    while True:
        client, addr = s.accept()
        print("SERVER: Got connection from", addr)
        send_handle(out_p, client.fileno(), worker_pid)
        client.close()


if __name__ == "__main__":
    c1, c2 = multiprocessing.Pipe()
    worker_p = multiprocessing.Process(target=worker, args=(c1, c2))
    worker_p.start()

    server_p = multiprocessing.Process(
        target=server, args=(("", 15000), c1, c2, worker_p.pid)
    )
    server_p.start()

    c1.close()
    c2.close()

###

"""
bash % python3 passfd.py
"""

###

# servermp.py
from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket


def server(work_address, port):
    # Wait for the worker to connect
    work_serv = Listener(work_address, authkey=b"peekaboo")
    worker = work_serv.accept()
    worker_pid = worker.recv()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(("", port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print("SERVER: Got connection from", addr)
        send_handle(worker, client.fileno(), worker_pid)
        client.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: server.py server_address port", file=sys.stderr)
        raise SystemExit(1)

    server(sys.argv[1], int(sys.argv[2]))

###

# workermp.py

from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import os
from socket import socket, AF_INET, SOCK_STREAM


def worker(server_address):
    serv = Client(server_address, authkey=b"peekaboo")
    serv.send(os.getpid())
    while True:
        fd = recv_handle(serv)
        print("WORKER: GOT FD", fd)
        with socket(AF_INET, SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print("WORKER: RECV {!r}".format(msg))
                client.send(msg)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: worker.py server_address", file=sys.stderr)
        raise SystemExit(1)

    worker(sys.argv[1])

###

# server.py

import socket
import struct


def send_fd(sock, fd):
    """
    Send a single file descriptor.
    """
    sock.sendmsg([b"x"], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack("i", fd))])
    ack = sock.recv(2)
    assert ack == b"OK"


def server(work_address, port):
    # Wait for the worker to connect
    work_serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    work_serv.bind(work_address)
    work_serv.listen(1)
    worker, addr = work_serv.accept()

    # Now run a TCP/IP server and send clients to worker
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(("", port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print("SERVER: Got connection from", addr)
        send_fd(worker, client.fileno())
        client.close()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: server.py server_address port", file=sys.stderr)
        raise SystemExit

    server(sys.argv[1], int(sys.argv[2]))

###

# worker.py
import socket
import struct


def recv_fd(sock):
    """
    Receive a single file descriptor
    """
    msg, ancdata, flags, addr = sock.recvmsg(1, socket.CMSG_LEN(struct.calcsize("i")))

    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS
    sock.sendall(b"OK")
    return struct.unpack("i", cmsg_data)[0]


def worker(server_address):
    serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    serv.connect(server_address)
    while True:
        fd = recv_fd(serv)
        print("WORKER: GOT FD", fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print("WORKER: RECV {!r}".format(msg))
                client.send(msg)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: worker.py server_address", file=sys.stderr)
        raise SystemExit(1)

    worker(sys.argv[1])

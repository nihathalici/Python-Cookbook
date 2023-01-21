# Exer-07-Creating-a-Thread-Pool

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor


def echo_client(sock, client_addr):
    """
    Handle a client connection
    """
    print("Got connection from", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


echo_server(("", 15000))

###

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


def echo_client(q):
    """
    Handle a client connection
    """
    sock, client_addr = q.get()
    print("Got connection from", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()


def echo_server(addr, nworkers):
    # Launch the client workers
    q = Queue
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()

    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))


echo_server(("", 15000), 128)

###

from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)
# Submit work to the pool
a = pool.submit(fetch_url, "http://www.python.org")
b = pool.submit(fetch_url, "http://www.pypy.org")


# Get the results back
x = a.result()
y = b.result()

###

from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


def echo_client(sock, client_addr):
    """
    Handle a client connection
    """
    print("Got connection from", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()


def echo_server(addr, nworkers):
    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        t = Thread(target=echo_client, args=(client_sock, client_addr))
        t.daemon = True
        t.start()


echo_server(("", 15000))

###

import threading

threading.stack_size(65536)

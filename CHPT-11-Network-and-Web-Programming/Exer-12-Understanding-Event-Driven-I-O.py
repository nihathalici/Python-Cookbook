# Exer-12-Understanding-Event-Driven-I-O


class EventHandler:
    def fileno(self):
        "Return the associated file descriptor"
        raise NotImplemented("must implement")

    def wants_to_receive(self):
        "Return True if receiving is allowed"
        return False

    def handle_receive(self):
        "Perform the receive operation"
        pass

    def wants_to_send(self):
        "Return True if sending is requested"
        return False

    def handle_send(self):
        "Send outgoing data"
        pass


import select


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


###

import socket
import time


class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode("ascii"), addr)


class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)


if __name__ == "__main__":
    handlers = [UDPTimeServer(("", 14000)), UDPEchoServer(("", 15000))]
    event_loop(handlers)

###

from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b"", ("localhost", 14000))

s.recvfrom(128)
s.sendto(b"Hello", ("localhost", 15000))

s.recvfrom(128)

###


class TCPServer(EventHandler):
    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        self.handler_list.append(self.client_handler(client, self.handler_list))


class TCPClient(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        # Remove myself from the event loop's handler list
        self.handler_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoClient(TCPClient):
    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


if __name__ == "__main__":
    handlers = []
    handlers.append(TCPServer(("", 16000), TCPEchoClient, handlers))
    event_loop(handlers)

###

from concurrent.futures import ThreadPoolExecutor
import os


class ThreadPoolHandler(EventHandler):
    def __init__(self, nworkers):
        if os.name == "posix":
            self.signal_done_sock, self.done_sock = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1", 0))
            server.listen(1)
            self.signal_done_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.signal_done_sock.connect(server.getsockname())
            self.done_sock, _ = server.accept()
            server.close()

        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)

    def fileno(self):
        return self.done_sock.fileno()

    # Callback that executes when the thread is done
    def _complete(self, callback, r):
        self.pending.append((callback, r.result()))
        self.signal_done_sock.send(b"x")

    # Run a function in a thread pool
    def run(self, func, args=(), kwargs={}, *, callback):
        r = self.pool.submit(func, *args, **kwargs)
        r.add_done_callback(lambda r: self._complete(callback, r))

    def wants_to_receive(self):
        return True

    # Run callback functions of completed work
    def handle_receive(self):
        # Invoke all pending callback functions
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
        self.pending = []


###


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class UDPFFibServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n,), callback=lambda r: self.respond(r, addr))

    def respond(self, result, addr):
        self.sock.sendto(str(result).encode("ascii"), addr)


if __name__ == "__main__":
    pool = ThreadPoolHandler(16)
    handlers = [pool, UDPFFibServer(("", 16000))]
    event_loop(handlers)

from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
for x in range(40):
    sock.sento(str(x).encode("ascii"), ("localhost", 16000))
    resp = sock.recvfrom(8192)
    print(resp[0])

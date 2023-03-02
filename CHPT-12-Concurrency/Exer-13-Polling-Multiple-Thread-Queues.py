# Exer-13-Polling-Multiple-Thread-Queues
import queue
import socket
import os


class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        # Create a pair of connected sockets
        if os.name == "posix":
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # Compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1", 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

        def fileno(self):
            return self._getsocket.fileno()

        def put(self, item):
            super().put(item)
            self._putsocket.send(b"x")

        def get(self):
            self._getsocket.recv(1)
            return super().get()


###

import select
import threading


def consumer(queues):
    """
    Consumer that reads data on multiple queues simultaneously
    """
    while True:
        can_read, _, _ = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print("Got:", item)


q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()
t = threading.Thread(target=consumer, args=([q1, q2, q3],))
t.daemon = True
t.start()

# Feed data to the queues
q1.put(1)
q2.put(10)
q3.put("hello")
q2.put(15)

###

import time


def consumer(queues):
    while True:
        for q in queues:
            if not q.empty():
                item = q.get()
                print("Got:", item)
    # Sleep briefly to avoid 100% CPU
    time.sleep(0.01)


###

import select


def event_loop(sockets, queues):
    while True:
        # polling with a timeout
        can_read, _, _ = select.select(sockets, [], [], 0.01)
        for r in can_read:
            handle_read(r)
        for q in queues:
            if not q.empty():
                item = q.get()
                print("Got:", item)

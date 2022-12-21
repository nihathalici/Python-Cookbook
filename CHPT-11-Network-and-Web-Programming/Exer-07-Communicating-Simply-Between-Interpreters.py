# Exer-07-Communicating-Simply-Between-Interpreters

from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')

from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
c.recv()

c.send(42)
c.recv()

c.send([1, 2, 3, 4, 5])
c.recv()

###

s = Listener('/tmp/myconn', authkey=b'peekaboo')

s = Listener(r'\\.\pipe\myconn', authkey=b'peekaboo')

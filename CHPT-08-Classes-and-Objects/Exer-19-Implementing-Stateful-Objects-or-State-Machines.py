# Exer-19-Implementing-Stateful-Objects-or-State-Machines

class Connection:
    def __init__(self):
        self.state = 'CLOSED'
    
    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')
    
    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('writing')
    
    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'\
    
    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'

class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate
    
    # Delegate to the state class
    def read(self):
        return self._state.read(self)
    
    def write(self, data):
        return self._state.write(self, data)
    
    def open(self):
        return self._state.open(self)
    
    def close(self):
        return self._state.close(self)

# Connection state base class
class ConnectionState:

    @staticmethod
    def read(conn):
        raise NotImplementedError()
    
    @staticmethod
    def write(conn, data):
        raise NotImplementedError()
    
    @staticmethod
    def close(conn):
        raise NotImplementedError()

# Implementation of different states
class ClosedConnectionState(ConnectionState):

    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
    
    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')
    
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
    
    @staticmethod
    def close(conn, data):
        raise RuntimeError('Already closed')

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')
    
    @staticmethod
    def write(conn, data):
        print('writing')
    
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')
    
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

c = Connection()
print(c._state)
# print(c.read())  # RuntimeError: Not open
c.open()
print(c._state)
print(c.read())
print(c.write('hello'))
print(c.close())
print(c._state)
    
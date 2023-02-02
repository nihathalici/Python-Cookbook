# Exer-11-Implementing-Publish-Subscribe-Messaging

from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


# Example of a task.  Any object with a send() method
class Task:
    ...

    def send(self, msg):
        ...


task_a = Task()
task_b = Task()

# Example of getting an exchange
exc = get_exchange("name")

# Examples of subscribing tasks to it
exc.attach(task_a)
exc.attach(task_b)

# Example of sending messages
exc.send("msg1")
exc.send("msg2")

# Example of unsubscribing
exc.detach(task_a)
exc.detach(task_b)

###

class DisplayMessages:
    def __init__(self):
        self.count = 0
    
    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg)

exc = get_exchange('name')
d = DisplayMessages()
exc.attach(d)

###

exc = get_exchange('name')
exc.attach(some_task)
try:
    ...
finally:
    exc.detach(some_task)

###

from contextlib import contextmanager
from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]

# Example of using the subscribe() method
exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    ...
    exc.send("msg1")
    exc.send("msg2")
    ...

# task_a and task_b detached here


class Task:
    ...

    def send(self, msg):
        ...


task_a = Task()
task_b = Task()

# Example of getting an exchange
exc = get_exchange("name")

# Examples of subscribing tasks to it
exc.attach(task_a)
exc.attach(task_b)

# Example of sending messages
exc.send("msg1")
exc.send("msg2")

# Example of unsubscribing
exc.detach(task_a)
exc.detach(task_b)

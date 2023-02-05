# Exer-12-Using-Generators-As-an-Alternative-to-Threads

# Two simple generator functions
def countdown(n):
    while n > 0:
        print("T-minus", n)
        yield
        n -= 1
    print("Blastoff!")


def countup(n):
    x = 0
    while x < n:
        print("Counting up", x)
        yield
        x += 1


from collections import deque


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        """
        Admit a newly started task to the scheduler
        """
        self._task_queue.append(task)

    def run(self):
        """
        Run until there are no more tasks
        """
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass


# Example use
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()

###

from collections import deque


class ActorScheduler:
    def __init__(self):
        self._actors = {}  # Mapping of names to actors
        self._msg_queue = deque()  # Message queue

    def new_actor(self, name, actor):
        """
        Admit a newly started actor to the scheduler and give it a name
        """
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        """
        Send a message to a named actor
        """
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        """
        Run as long as there are pending messages.
        """
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


# Example use
if __name__ == "__main__":

    def printer():
        while True:
            msg = yield
            print("Got:", msg)

    def counter(sched):
        while True:
            # Receive the current count
            n = yield
            if n == 0:
                break
            # Send to the printer task
            sched.send("printer", n)
            # Send the next count to the counter task (recursive)
            sched.send("counter", n - 1)


sched = ActorScheduler()
# Create the initial actors
sched.new_actor("printer", printer())
sched.new_actor("counter", counter(sched))

# Send an initial message to the counter to initiate
sched.send("counter", 10000)
sched.run()

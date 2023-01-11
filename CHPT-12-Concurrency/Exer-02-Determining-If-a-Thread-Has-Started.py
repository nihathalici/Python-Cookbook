# Exer-02-Determining-If-a-Thread-Has-Started

from threading import Thread, Event
import time

# Code to execute in an independent thread
def countdown(n, started_evt):
    print("countdown starting")
    started_evt.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print("Launching countdown")
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print("countdown is running")

###

import threading
import time


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """
        Run the timer and notify waiting threads after each interval
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        """
        Wait for the next tick of the timer
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


# Example use of the timer
ptimer = PeriodicTimer(5)
ptimer.start()

# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print("T-minus", nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print("Counting", n)
        n += 1


threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()

###

# Worker thread
def worker(n, sema):
    # Wait to be signaled
    sema.acquire()
    # Do some work
    print("Working", n)


# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema))
    t.start()

sema.release()
sema.release()

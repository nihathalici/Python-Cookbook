# Exer-08-Performing-Simple-Parallel-Programming

"""
logs/
       20120701.log.gz
       20120702.log.gz
       20120703.log.gz
       20120704.log.gz
       20120705.log.gz
       20120706.log.gz
       ...

124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304 -
...
"""

#
# findrobots.py

import gzip
import io
import glob


def find_robots(filename):
    """
    Find all of the hosts that access robots.txt in a single log file
    """
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding="ascii"):
            fields = line.split()
            if fields[6] == "/robots.txt":
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    """
    Find all hosts across and entire sequence of files
    """
    files = glob.glob(logdir + "/*.log.gz")
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


if __name__ == "__main__":
    robots = find_all_robots("logs")
    for ipaddr in robots:
        print(ipaddr)

###

# findrobots.py

import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):
    """
    Find all of the hosts that access robots.txt in a single log file
    """
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding="ascii"):
            fields = line.split()
            if fields[6] == "/robots.txt":
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    """
    Find all hosts across and entire sequence of files
    """
    files = glob.glob(logdir + "/*.log.gz")
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == "__main__":
    robots = find_all_robots("logs")
    for ipaddr in robots:
        print(ipaddr)

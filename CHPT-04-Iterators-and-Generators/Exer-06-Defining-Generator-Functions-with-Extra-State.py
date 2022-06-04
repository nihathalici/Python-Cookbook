# Exer-06-Defining-Generator-Functions-with-Extra-State

from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

with open('em_ad.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

###

f = open('em_ad.txt')
lines = linehistory(f)
#next(lines)  # TypeError
it = iter(lines)
next(it)
next(it)

# Exer-07-Taking-a-Slice-of-an-Iterator

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# c[10:20] # TypeError

import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

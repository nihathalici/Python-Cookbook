# Exer-10-Iterating-Over-the-Index-Value-Pairs-of-a-Sequence

my_list = ['a', 'b', 'c']

for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)
"""
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))
"""

word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip()lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

###
        
lineno = 1
for line in f:
    # Process line
    lineno += 1
###

for lineno, line in enumerate(f):
    # Process line

###

data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

for n, (x, y) in enumerate(data):  # Correct!

for n, x, y in enumerate(data):  # Error

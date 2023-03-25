# Exer-05-Getting-the-Terminal-Size

import os

sz = os.get_terminal_size()

print(sz)
print(sz.columns)
print(sz.lines)

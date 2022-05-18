# Exer-16-Reformatting-Text-to-a-Fixed-Number-of-Columns.py

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(textwrap.fill(s, 70))

print(textwrap.fill(s, 40))

print(textwrap.fill(s, 40, initial_indent='   '))

print(textwrap.fill(s, 40, subsequent_indent='   '))

###

import os

print( os.get_terminal_size().columns )
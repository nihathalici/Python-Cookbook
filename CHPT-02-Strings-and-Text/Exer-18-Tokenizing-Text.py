# Exer-18-Tokenizing-Text.py

text = 'foo = 23 + 42 * 10'

import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

#scanner = master_pat.scanner('foo = 42')
#scanner.match()
#print( _.lastgroup, _.group() )  # Error

from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

print('***********')

tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS' )

for tok in tokens:
    print(tok)

###

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))  # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ]))  # Incorrect

###
print('------------------------')
PRINT = r'(P<PRINT>print)'
NAME = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'): #???
    print(tok)



















# -*- coding: utf-8 -*-.

import re

"""tokenizer
named re token
"""
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES= r'(?P<TIMES>\*)'
DIV  = r'(?P<DIV>/)'
EQ   = r'(?P<EQ>=)'
WS   = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, MINUS, TIMES, DIV, EQ, WS]))

from collections import namedtuple
Token = namedtuple('Token', ['type', 'value'])
"""re scanner
1. identify every possible text sequence that might appear in the input with a correponding
   re pattern. If any nonmatching text is found, scanning will stop.   
2. re pattern match according to order in pattern ==> longest pattern first
3. substring in other pattern   PRINT = r'(?P<PRINT>PRINT)  NAME= r'(?P<NAME>[a-zA-Z_][a-zA-Z_]*) 
   printer will be match to print and er
4. advanced tokenizer PLY (lex and yacc) and PyParsig
"""
def generateToken(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generateToken(master_pat, 'y1 = 5*x1 + 4*x2'):
    print (tok)

print("filter out whitespace")
rtokens = (tok for tok in generateToken(master_pat, 'y2 = x3*4 + x1/4 - 2/23*x2')
           if tok.type != 'WS')
for t in rtokens:
    print (t)


if __name__=='__main__': 
    main()

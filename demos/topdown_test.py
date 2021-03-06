'''Run Example 4.1 from Aho & Ullman p. 292-293, printing the steps to stdout.
'''

import sys
from cfg import aho_ullman, core

CFG = core.ContextFreeGrammar

G = CFG('''
E -> T+E
E -> T
T -> F*T
T -> F
F -> a
''')

w = [core.Terminal(a) for a in 'a+a']

print 'G:'
print G
print
print 'w =', ''.join(map(str, w))
print

try:
    parse = aho_ullman.topdown_backtrack_parse(G, w, sys.stdout)
    print
    print 'Parse tree:', aho_ullman.LeftParse(G, parse).tree()
except aho_ullman.ParseError, e:
    print e

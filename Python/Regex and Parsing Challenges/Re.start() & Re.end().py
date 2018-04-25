#!/bin/python3

import re

s, k = input(), input()
#method 1
"""
if k in s:
    print( *[ (el.start(), el.start()+len(k)-1) for el in re.finditer( r"(?={})".format( k), s)], sep="\n")
else:
    print( "(-1, -1)")
"""

#method2
pattern = re.compile(k)
res = pattern.search( s)
if res:
    while res:
        print( "({0}, {1})".format( res.start(), res.end() - 1))
        res = pattern.search( s, res.start() + 1)
else:
    print( "(-1, -1)")
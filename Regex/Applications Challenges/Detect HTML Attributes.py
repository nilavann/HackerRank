#!/bin/python3

import re
from collections import defaultdict

Regex = r'<(\w+?)(|\s+[^>]+)>'
htmlPage = "\n".join( [ input() for _ in range( int( input()))])
elements = re.findall( Regex, htmlPage)
elementDict = defaultdict( set)
for element in elements:
    tag, attrs = element
    elementDict[ tag].update( re.findall( r'((?<= )[a-z]+)=', attrs))
for i in sorted( elementDict.items()):
    print( i[0], ",".join( sorted(i[1])), sep = ":")
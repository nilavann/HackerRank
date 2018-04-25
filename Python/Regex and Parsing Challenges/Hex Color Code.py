#!/bin/python3

import re

for _ in range( int( input())):
    [ print( j) for j in re.findall( r"[\s:](#[0-9a-fA-F]{3,6})", input())]

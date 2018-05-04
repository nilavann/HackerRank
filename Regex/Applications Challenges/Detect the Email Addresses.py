#!/bin/python3

import re

pessage = "\n".join( [ input() for _ in range( int( input()))])
reult = list( set( re.findall( r"([\w.]+@(?:[\w]+\.){1,}(?:com|in|org))", pessage)))
print( ";".join( sorted( reult)))
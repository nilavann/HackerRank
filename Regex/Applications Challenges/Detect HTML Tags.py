#!/bin/python3
import re

regex = r'<\s*(\w+)>?'
tags = list()
for _ in range( int( input())):
    tags.extend(re.findall( regex, input()))
print( *sorted( set( tags)), sep = ";")
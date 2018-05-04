#!/bin/python3

import re

sentence = "\n".join( [ input() for _ in range( int( input()))])
for _ in range( int( input())):
    Regex = r"(" + input()[:-2] + "(?:ze|se))"
    print( len( re.findall( Regex, sentence)))
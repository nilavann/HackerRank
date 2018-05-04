#!/bin/python3

import re

Regex = r"^(hackerrank)?(.*?)(hackerrank)?$"
for _ in range( int( input())):
    result = re.findall( Regex, input())
    if( (result[0][0] == "hackerrank" and result[0][2] == "hackerrank") or (result[0][0] == "hackerrank" and result[0][2] == "" and result[0][1] == "")):
        print( 0)
    elif( result[0][0] == "hackerrank"):
        print( 1)
    elif( result[0][2] == "hackerrank"):
        print( 2)
    else:
        print( -1)
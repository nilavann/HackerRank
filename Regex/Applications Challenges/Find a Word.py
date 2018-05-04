#!/bin/python3

import re
sentences = " ".join( [ input() for _ in range( int( input()))])
for _ in range( int( input())):
    testWord = input()
    print( len( re.findall( "(?<![\w\d])"+testWord+"(?![\w\d])", sentences)))
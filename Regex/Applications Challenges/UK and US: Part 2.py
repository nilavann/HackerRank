#!/bin/python3

import re

sentence = "\n".join( [ input() for _ in range( int( input()))])
for _ in range( int( input())):
    print( len( re.findall( "\\b" + input().replace("our","ou?r") + "\\b", sentence, re.I)))
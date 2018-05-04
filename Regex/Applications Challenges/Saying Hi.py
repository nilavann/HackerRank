#!/bin/python3

import re

Regex = r"^HI [^D].*"
for _ in range( int( input())):
    sentence = input()
    if( bool( re.match( Regex, sentence, re.I))):
        print( sentence)
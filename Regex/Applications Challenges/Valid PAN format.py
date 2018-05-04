#!/bin/python3

import re

Regex = r"[A-Z]{5}\d{4}[A-Z]"
for _ in range( int( input())):
    print( "YES" if( bool( re.match( Regex, input()))) else "NO")
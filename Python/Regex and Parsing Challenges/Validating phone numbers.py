#!/bin/python3

import re

for _ in range( int( input())):
    print( "YES" if( bool( re.match( r"^(7|8|9)[0-9]{9}$", input()))) else "NO")
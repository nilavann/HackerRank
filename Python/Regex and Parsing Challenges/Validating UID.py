#!/bin/python3

import re

for _ in range( int( input())):
    uid = "".join( sorted( input()))
    if( len( uid) == 10 and not bool( re.search( r"(.)\1", uid)) and bool( re.match( r"^[\d]{3,8}[A-Z]{2,}[a-z]*$", uid))):
        print( "Valid")
    else:
        print( "Invalid")
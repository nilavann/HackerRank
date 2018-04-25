#!/bin/python3

import re

isequalgroup = re.compile( r"^(.{4}-){3}.{4}$").match
checkisvalid = re.compile( r"^[456]\d{15}$").match
consecutive = re.compile( r"(.)\1{3}").search
for _ in range( int( input())):
    ccnumber = input()
    if( isequalgroup( ccnumber)):
        ccnumber = re.sub( "-", "", ccnumber)
    if( checkisvalid(ccnumber) and not consecutive(ccnumber)):
        print( "Valid")
    else:
        print( "Invalid")
    
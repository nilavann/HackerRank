#!/bin/python3

import re

#check 0-9.\d+,10-89.\d+,90.0+ same as for 180
Regex = r"^\([+-]?(?:(?:[1-8]\d|\d)(?:\.\d+)?|90(?:\.0+)?), [+-]?(?:(?:1[0-7]\d|\d\d|\d)(?:\.\d+)?|180(?:\.0+)?)\)$"
for _ in range( int( input())):
    print( "Valid" if( bool( re.match( Regex, input()))) else "Invalid")
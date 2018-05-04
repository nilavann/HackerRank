#!/bin/python3
import re

regex = r"^(_|\.)[0-9]+[a-zA-Z]*_?$"
for _ in range( int( input())):
    print( "VALID") if(re.match( regex, input())) else print( "INVALID")
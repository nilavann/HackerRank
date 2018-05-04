#!/bin/python3

import re

Regex = r"^(\d+)( |-)(\d+)\2(\d+)$"
for _ in range( int( input())):
    result = re.match( Regex, input())
    print( "CountryCode={},LocalAreaCode={},Number={}".format(result.group(1), result.group(3), result.group(4)))
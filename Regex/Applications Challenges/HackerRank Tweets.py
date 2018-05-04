#!/bin/python3

import re

Regex = r"hackerrank"
hackerrankOcuureanceCount = 0
for _ in range( int( input())):
    hackerrankOcuureanceCount += len( re.findall( Regex, input(), re.I))
print( hackerrankOcuureanceCount)
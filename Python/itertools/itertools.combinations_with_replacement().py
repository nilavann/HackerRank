#!/bin/python3

from itertools import combinations_with_replacement
s, n = input().strip().split()
# loop combinations_with_replacement() conv tuple to string, unpack 
print( *[ "".join(element) for element in combinations_with_replacement\
         ( sorted( s), int( n))], sep = "\n")
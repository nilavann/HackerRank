#!/bin/python3

from itertools import combinations
s, n = input().strip().split()
# loop from i to n conv tuple to string, unpack 
print( *[ "".join(element) for i in range( 1, int(n) + 1) \
	for element in combinations( sorted( s), i)], sep = "\n")
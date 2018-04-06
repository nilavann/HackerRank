#!/bin/python3

from itertools import permutations
s, n = input().strip().split()
# convert the tuples as string , sort, unpack
print( *sorted( [ "".join(element) \
	for element in permutations( s, int(n))]), sep = "\n")

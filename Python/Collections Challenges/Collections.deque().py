#!/bin/python3

from collections import deque
d = deque()

for _ in range( int( input())):
    operation = input().split()
    eval( 'd.' + operation[0] + '(' + "".join(operation[1:]) + ')')
print( *d)
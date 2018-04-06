#!/bin/python3

from collections import defaultdict
d = defaultdict(list)
n, m = list( map( int, input().split()))
for i in range( 1, n + 1):
    d[input()].append(i)
for _ in range(m):
    key = input()
    if( key in d):
        print( *d[key])
    else:
        print( -1)
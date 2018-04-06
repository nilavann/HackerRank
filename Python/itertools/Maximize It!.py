#!/bin/python3
import itertools
k, m = map(int, input().strip().split())
n = ( list( map( int, input().split()))[1:] \
	for _ in range(k))
print( max ( [ sum( map( lambda x: x ** 2, i))%m \
	for i in itertools.product(*n)]))
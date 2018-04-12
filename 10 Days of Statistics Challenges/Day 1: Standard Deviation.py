#!/bin/python3

import math

n = int( input())
x = list( map( int, input().split()))
mean = sum( x) / n
print( round( math.sqrt( sum( ( ( i - mean) ** 2 for i in x)) / n), 1))
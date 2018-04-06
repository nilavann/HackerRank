#!/bin/python3
import statistics as st

# find median
def findMedian( elements):
    size = len( elements)
    center = size // 2
    return  ( elements[ center] + elements[ center - 1]) // 2 \
           if( size % 2 == 0) else elements[ center]

n = int( input())
x = list( map( int, input().strip().split()))
f = list( map( int, input().strip().split()))
s = []
for i, j in zip(x,f):
    s += [i]*j
s.sort()
length = len( s)
if( length % 2 == 0):
    Q1 = findMedian( s[ :length // 2])
    Q3 = findMedian( s[ length // 2:])
else:
    Q1 = findMedian( s[ :length // 2])
    Q3 = findMedian( s[ (length // 2) + 1:])
print( round( float(Q3 - Q1), 1))
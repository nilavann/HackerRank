#!/bin/python3

n = int( input())
X = list( map( int, input().strip().split()))
W = list( map( int, input().strip().split()))

#weighted mean 

print( "{:.1f}".format( sum( [ i * j for i, j in zip( X, W)]) / sum( W)))
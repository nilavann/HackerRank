#!/bin/python3

col, row = list( map( int, input().split()))
marks = []
for _ in range( row):
    marks.append( list( map( float, input().split())))
    #print( marks)
for i in zip( *marks):
    print( sum(i)/row)
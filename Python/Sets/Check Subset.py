#!/bin/python3

for _ in range( int( input())):
    setA, setB = [ set( map( int, input().strip().split())) for _ in range(4)][1::2]
    print( not bool(setA.difference(setB)))
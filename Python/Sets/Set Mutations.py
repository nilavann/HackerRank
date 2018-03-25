#!/bin/python3

n = int(input())
setA = set( map( int, input().split()))
for _ in range( int( input())):
    operation = input().split()
    #storing input set into setB
    setB = set( map( int, input().split()))
    # using eval
    eval("setA." + operation[0] + "(setB)")
print( sum(setA))
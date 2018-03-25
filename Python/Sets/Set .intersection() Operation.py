#!/bin/python3

setA, setB = [ set(input().split()) for _ in range(4)][1::2]
print( len(setA.intersection(setB)))
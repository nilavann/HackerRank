#!/bin/python3

setA, setB = [ set(input().split()) for _ in range(4)][1::2]
#symmetric differnce return the items both its that not present in both

# method 1
# print( len(setA.symmetric_difference(setB)))

# method 2
print( len(setA^setB))
#!/bin/python3

from collections import Counter
# counter counts accurance of all values in given list and store as dict
n = int( input())
shoes = Counter( map( int, input().split()))
cost = 0
for _ in range( int( input())):
    size, price = list( map( int, input().split()))
    if( shoes[size] != 0):
        cost += price
        shoes[size] -= 1
print( cost)

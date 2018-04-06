#!/bin/python3

import collections

n = int( input())
orderedDictonary = collections.OrderedDict()
for _ in range(n):
    item, middle, price = input().rpartition(' ')
    orderedDictonary[item] = orderedDictonary.get(item,0) + int( price)
for item, price in orderedDictonary.items():
    print( item, price)
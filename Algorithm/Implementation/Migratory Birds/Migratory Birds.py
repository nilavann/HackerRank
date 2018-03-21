#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    birdCount = [ar.count(i) for i in [1,2,3,4,5]]
    return birdCount.index(max(birdCount)) + 1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
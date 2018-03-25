#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    return( sum((ar.count(color)//2 for color in set(ar))))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

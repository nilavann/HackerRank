#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    # using enumerate and list comprehansion
    return len( [1 for i,num1 in enumerate(ar) for j,num2 in enumerate(ar) \
         if( ( i < j) and ( num1 + num2) % k == 0)])
    print( l)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)

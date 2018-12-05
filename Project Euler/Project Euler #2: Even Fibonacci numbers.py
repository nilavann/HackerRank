#!/bin/python3

import sys
import math

# we know that every 3 element in Fibonacci series is divisible by 2
# 0,2,8,34
# 4 * 8   + 2 = 34
# 4 * 34  + 8 = 144
# 4 * 144 + 34 = goes on
# 4 * n2  + n1 = n3
# 4 * n3  + n2 = n4
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    i = 0
    fibonacciNumber = 2
    while( fibonacciNumber <= n):
        temp = fibonacciNumber
        sum += fibonacciNumber
        fibonacciNumber = 4 * fibonacciNumber + i
        i = temp
    print( sum)

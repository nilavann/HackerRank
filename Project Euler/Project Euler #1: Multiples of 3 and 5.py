#!/bin/python3

import sys

sum = 0

#To get n value total elements in the seq
def highestDivisable( diviser, n):
    return ( n - 1) // diviser

#To check weather they are even or odd
def gethighestDivisable( diviser, n):
    global sum
    res = highestDivisable( diviser, n)
    if( res % 2 != 0):
        if( diviser == 15):
            sum -= diviser + ( res - 1) * diviser
        else:
            sum += diviser + ( res - 1) * diviser
        return res - 1
    return res
       
#Calculate sum of the sequence
def sumOfSequence( a, d, n):
    return ( ( n // 2) * ( 2 * a + ( n - 1) * d))

t = int(input().strip())
for a0 in range(t):
    sum = 0
    n = int(input().strip())
    a3 = 3
    a5 = 5
    a15 = 15
    d3 = 3
    d5 = 5
    d15 = 15
    n3 = gethighestDivisable( 3, n)
    n5 = gethighestDivisable( 5, n)
    n15 = gethighestDivisable( 15, n)
    print( sumOfSequence( a3, d3, n3) + sumOfSequence( a5, d5, n5) - sumOfSequence( a15, d15, n15) + sum)
    
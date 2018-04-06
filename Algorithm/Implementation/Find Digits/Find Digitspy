#!/bin/python3

import sys

def findDigits(n):
    # Complete this function
    return sum( 1 for i in str( n) if( ( int( i) != 0) and ( n % int( i) == 0)))
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)

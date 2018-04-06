#!/bin/python3

import sys

def beautifulDays(i, j, k):
    # Complete this function
    return len( [ 1 for number in range( i, j + 1) \
                 if( abs( number - int( str( number)[::-1])) % k == 0)])

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)

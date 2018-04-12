#!/bin/python3

from collections import deque

for _ in range( int( input())):
    d = deque()
    n = int( input())
    d.extend( map( int, input().split()))
    # take the max element from both ends as top
    top, i = max( d[0], d[n - 1]), 0
    # remove top element from list
    d.popleft() if( top == d[0]) else d.pop()
    for _ in range(n - 1):
        # same as before
        maxValue = max( d[i], d[len(d) - 1])
        if ( d[len(d) - 1] == maxValue) and ( top >= d[len(d) - 1]):
            top = d[len(d) - 1]
            d.pop()
        elif ( d[i] == maxValue) and ( top >= d[i]):
            top = d[i]
            d.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")
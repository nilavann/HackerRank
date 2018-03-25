#!/bin/python3

k = int(input())
roomNos = list( map(int, input().split()))
'''
# method 1
# Since the captons room present only once
for i in set(roomNos):
    roomNos.remove(i)
    if(i not in roomNos):
        print( i)
        break
'''

# method 2
print( ( sum( set( roomNos)) * k - sum( roomNos)) // ( k -1))
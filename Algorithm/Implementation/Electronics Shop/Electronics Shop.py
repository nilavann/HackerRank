#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    '''
    # method 1
    priceList = [keyboardPrice + drivesPrice for keyboardPrice in keyboards \
    for drivesPrice in drives if(keyboardPrice + drivesPrice) <= s]
    if not priceList: 
        return -1
    return max(priceList)
    '''
    # method 2 
    result = -1
    for i in sorted(keyboards, reverse = True):
        for j in sorted(drives):
            if i + j > s:
                break
            result = max(result, i + j)
    return result
    
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)

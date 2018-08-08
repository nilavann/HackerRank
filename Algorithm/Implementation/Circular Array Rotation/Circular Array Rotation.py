#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, m, k):
    #The array full rotation is length of array
    arryLen = len(a)
    rotation = k % arryLen
    tempList = []
    tempList.extend( a[arryLen - rotation:])
    tempList.extend( a[:arryLen - rotation])
    return list( map( lambda x: tempList[x], m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    m = []

    for _ in range(q):
        m_item = int(input())
        m.append(m_item)

    result = circularArrayRotation(a, m, k)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

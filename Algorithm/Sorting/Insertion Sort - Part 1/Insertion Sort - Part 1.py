#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    num = arr[-1]
    i = n - 2
    while(num < arr[i] and i >= 0):
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1;
    arr[i + 1] = num
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
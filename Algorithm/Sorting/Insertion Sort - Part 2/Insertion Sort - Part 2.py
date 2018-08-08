#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        for j in range ( 0, i):
            if( arr[i] < arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        print( *arr)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
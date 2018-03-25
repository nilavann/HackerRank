#!/bin/python3

import sys

def equalizeArray(arr):
    # Complete this function
    return len(arr) - max( [ arr.count(num) for num in set(arr)])
        
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)

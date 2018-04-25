#!/bin/python3

import sys

def jumpingOnClouds(c):
    # Complete this function
    jumps = 0
    clouds = -1
    for i in c:
        # non thuder clods increment
        if i  == 0:
            clouds += 1
        # thuder clouds (+ 1) since we jump thuder cloud other find min jumps
        else:
            jumps += clouds // 2
            jumps += ( clouds % 2 ) + 1
            clouds = -1
    jumps +=  clouds // 2
    jumps +=  clouds % 2
    return jumps

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c)
    print(result)

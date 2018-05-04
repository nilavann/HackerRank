#!/bin/python3

import sys

def countingValleys(n, s):
    # Complete this function
    noOfvalleys = 0
    steps = 0
    for i, step in enumerate(s):
        steps += -1 if step == "D" else 1
        # since if its D he still not corrsed a valley 
        if( steps == 0 and step == "U"):
            noOfvalleys += 1
    return noOfvalleys

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)

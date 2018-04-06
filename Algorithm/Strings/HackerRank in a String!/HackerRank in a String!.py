#!/bin/python3

import sys

def hackerrankInString(s):
    # Complete this function
    key = "hackerrank"
    i = 0
    for char in s:
        if( i < 10 and char.lower() == key[i]):
            i += 1
    return "YES" if( i == 10) else "NO"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
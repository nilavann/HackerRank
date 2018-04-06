#!/bin/python3

import sys

def repeatedString(s, n):
    # Complete this function
    return ( ( n // len(s)) * s.count("a")) + ( s[:( n % len(s))].count("a"))
if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)

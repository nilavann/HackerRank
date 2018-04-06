#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    i = 0
    while( i < len(s)):
        if( i >= 1 and s[i] == s[i - 1]):
            i -= 1;
        elif( i < len(s) - 1 and s[i] == s[i + 1]):
            s = s[:i] + s[i + 2:]
        else:
            i += 1
    return "Empty String" if( s == "") else s

s = input().strip()
result = super_reduced_string(s)
print(result)

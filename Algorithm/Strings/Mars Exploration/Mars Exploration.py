#!/bin/python3

import sys

def marsExploration(s):
    # Complete this function
    '''
    # method 1
    error = 0
    for i,c in enumerate(s):
        error += ( 1 if( c == "SOS"[i % 3]) else 0)
    return error
    '''
    
    # method 2
    
    return ( len( [ 1 for x, y in zip(s, "SOS"*(len(s)//3)) if( x != y)]))

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)

#!/bin/python3

from datetime import datetime
import sys

def time_delta(t1, t2):
    # Complete this function
    givenFormat = "%a %d %b %Y %H:%M:%S %z"
    return( int ( abs( datetime.strptime( t1, givenFormat) - datetime.strptime( t2, givenFormat)).total_seconds()))
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)

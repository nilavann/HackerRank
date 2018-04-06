#!/bin/python3

import sys

def viralAdvertising(n):
    # Complete this function
    likes, totalLikes = 2, 2
    for _ in range( n - 1):
        #increment
        likes = ( likes * 3) // 2
        totalLikes += likes
    return totalLikes
    

if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)

#!/bin/python3

#function to find mean, upperHAlf, lowerHalf
def findMedianAndList( elements, size):
    center = size // 2
    Q = ( elements[ center] + elements[ center - 1]) // 2 \
        if( size % 2 == 0) else elements[ size // 2]
    if( size % 2 == 0):
        return elements[:center], Q, elements[center:]
    else:
        return elements[:center], Q, elements[center + 1:]
    
def findMedian( elements, size):
    center = size // 2
    return ( elements[ center] + elements[ center - 1]) // 2 \
           if( size % 2 == 0) else elements[ size // 2]

# inputs
n = int( input())
elements = list( sorted( map( int, input().split())))

# quartiles 2
lowerHalf, Q2, upperHalf = findMedianAndList(elements, n)

# quartiles 1,3
Q1 = findMedian(lowerHalf, len(lowerHalf))
Q3 = findMedian(upperHalf, len(upperHalf))

print( Q1, Q2, Q3, sep = "\n")
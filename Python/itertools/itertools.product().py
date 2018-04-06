#!/bin/python3
#Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
A = list( map( int, input().strip().split()))
B = list( map( int, input().strip().split()))
# print the unpacked list
print( *list( product(A,B)))
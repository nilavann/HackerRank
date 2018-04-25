#!/bin/python3

import numpy as np

row = int( input())
matA = np.array( [ list( map( int, input().split())) for _ in range( row)])
matB = np.array( [ list( map( int, input().split())) for _ in range( row)])
print( np.dot( matA, matB))
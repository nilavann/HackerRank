#!/bin/python3

import numpy as np

np.set_printoptions(legacy='1.13')
row, col = list( map( int, input().split()))
mat = np.array( [ list( map( int, input().split())) for _ in range( row)])
print( np.mean( mat, axis = 1), np.var( mat, axis = 0), np.std( mat), sep = "\n")
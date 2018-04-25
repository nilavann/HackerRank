#!/bin/python3

import numpy as np

row, col = list( map( int, input().split()))
mat = np.array( [ list( map( int, input().split())) for _ in range( row)])
print( np.max( np.min( mat, axis = 1)))
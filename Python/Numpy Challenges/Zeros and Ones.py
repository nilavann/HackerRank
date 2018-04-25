#!/bin/python3
import numpy as np

shopeOfArray = tuple( map( int, input().split()))
print( np.zeros( shopeOfArray, dtype = np.int))
print( np.ones( shopeOfArray, dtype = np.int))
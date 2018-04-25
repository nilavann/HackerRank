#!/bin/python3

import numpy as np

matA = np.array( list( map( int, input().split())))
matB = np.array( list( map( int, input().split())))
print( np.inner( matA, matB), np.outer( matA, matB), sep = "\n")
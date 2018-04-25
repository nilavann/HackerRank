#!/bin/python3

import numpy as np

arrA = np.array( [ list( map( float, input().split())) \
                  for _ in range( int( input()))])
print( round( np.linalg.det( arrA), 2))
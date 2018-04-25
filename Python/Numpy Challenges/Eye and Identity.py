#!/bin/python3

import numpy as np
np.set_printoptions(sign = " ")
row, col = list( map( int, input().split(" ")))
print( np.eye( row, col))
#!/bin/python3

import numpy as np

p = np.array( list( map( float, input().split())))
x = float( input())
print( np.polyval( p, x))
#!/bin/python3

import numpy as np

np.set_printoptions(sign = " ")
mat = np.array( input().split() , float)
print( np.floor( mat), np.ceil( mat), np.rint( mat), sep = "\n")

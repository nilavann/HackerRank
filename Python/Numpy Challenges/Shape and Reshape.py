#!/bin/python3

import numpy as np
#create list from input and feed it to reshape
print( np.reshape( list( map( int, input().split())), (3,3)))
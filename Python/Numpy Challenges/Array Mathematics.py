#!/bin/python3

import numpy as np

row, col = list( map( int, input().split()))
a = np.array( [ list( map( int, input().split())) for _ in range(row)])
b = np.array( [ list( map( int, input().split())) for _ in range(row)])
print( a + b, a - b, a * b, a // b, a % b, a ** b, sep = "\n")
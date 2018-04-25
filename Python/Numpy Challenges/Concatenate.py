#!/bin/python3

import numpy as np

n, m, p = list( map( int, input().strip().split()))

arrn = np.array( [ list( map( int, input().strip().split())) for _ in range(n)])
arrm = np.array( [ list( map( int, input().strip().split())) for _ in range(m)])
print( np.concatenate( (arrn, arrm)))
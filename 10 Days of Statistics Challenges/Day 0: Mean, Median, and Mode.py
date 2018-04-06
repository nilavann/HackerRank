#!/bin/python3
import itertools
import numpy as np
from scipy import stats
length = int(input())
values = list(map(int, input().split()))

# method 1

'''

# mean
print(sum(values)/length)
values.sort()
# median
print((values[length // 2] + values[(length // 2) - 1])/2 if(length%2 == 0) else values[length//2])
grouped = [[key, len( list( elements))] for key,elements in itertools.groupby(values)]
max = [0, 0]
for i in grouped:
    if( i[1] > max[1]):
        max = i
# mode
print( max[0])
'''

# method 2

# mean, median, mode
print( np.mean( values), np.median( values), *( stats.mode( values)[0]), sep ="\n")
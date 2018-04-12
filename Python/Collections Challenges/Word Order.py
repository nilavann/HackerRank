#!/bin/python3
from collections import OrderedDict

orderdict = OrderedDict()
for _ in range( int( input())):
    key = input()
    orderdict[ key] = orderdict.get( key, 0) + 1
print( len(orderdict))
print( *orderdict.values())
#!/bin/python3

import itertools
n = int(input())
result = [ 1  if( 'a' in i) else 0 for i in itertools.combinations( input().split(), int( input()))]
print( sum( result)/len( result))
#!/bin/python3

from itertools import groupby

print( *[ ( len( list( elements)), int(element)) for element, elements in groupby( input().strip())])
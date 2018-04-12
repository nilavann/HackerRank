#!/bin/python3

n = int( input())

elements = input().split()

print( all( map( lambda x: int(x) > 0, elements)) and \
      any( element == element[::-1] for element in elements))
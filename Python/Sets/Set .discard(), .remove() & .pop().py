#!/bin/python3
n = input()
s = set(map(int, input().split())) 
for _ in range( int( input())):
    '''
    # method 1
    # split input 
    operation = input().strip().split()
    eval( "s."+ operation[0] + "(" + str(*operation[1:]) + ")")
    '''
    eval("s.{0}({1})".format(*input().split()+[""]))
print( sum( s))
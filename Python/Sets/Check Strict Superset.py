#!/bin/python3

setA = set( input().split())
#method 1
# print( all( not bool( set( input().split()).difference( setA)) for _ in range( int( input()))))

# method 2
for _ in range( int( input())):
    setB = set( input().split())
    if( bool( setB.difference( setA))):
        print( "False")
        break
else:
    print( "True")
        
       
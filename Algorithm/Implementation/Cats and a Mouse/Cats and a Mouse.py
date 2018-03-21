#!/bin/python3

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    #
    # Write your code here.
    # 
    return ( "Mouse C"  if( abs( x - z) == abs( y - z)) else "Cat B" if( abs( x - z) > abs( y - z)) else "Cat A")


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()

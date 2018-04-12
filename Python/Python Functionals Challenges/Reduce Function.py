#!/bin/python3

def product(fracs):
    print( fracs)
    t = reduce( lambda x,y: x*y,fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator
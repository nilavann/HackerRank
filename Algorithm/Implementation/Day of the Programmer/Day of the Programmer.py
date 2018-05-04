#!/bin/python3

import sys

def solve(year):
    # Complete this function
    # julien calender
    if( year < 1918):
        feb = 29 if( year % 4 == 0) else 28
    # Gregorian calendar
    elif(year > 1918):
        feb = 29 if( year % 400 == 0 or ( year%4 == 0 and year % 100 != 0)) else 28
    else:
        feb = 15
        # since feb only changes others mon sum of days 215
    return str(256 - ( feb + 215)) + ".09." + str(year)
year = int(input().strip())
result = solve(year)
print(result)

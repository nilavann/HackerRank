#!/bin/python3

from collections import namedtuple

n = int( input())

# method 1
'''
students = namedtuple( "student", "MARKS")
index = input().strip().split().index("MARKS")
print( "{:.2f}".format(sum( [ int(student.MARKS) for _ in range(n) for student in [students(input().strip().split()[index])]]) / n))
'''

# method 2
totalMarks = 0
students = namedtuple( "student", input().strip().split())
for _ in range(n):
    value1, value2, value3, value4 = input().strip().split()
    student = students( value1, value2, value3, value4)
    totalMarks += int( student.MARKS)
print( "{:2f}".format( totalMarks / n))

#!/bin/python3

import re

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix, expression = [], ""
for _ in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)
for row in zip(*matrix):
    expression+= "".join(row);
print( re.sub( r"(?<=[0-9a-zA-Z])([^0-9a-zA-Z]+)(?=[a-zA-Z0-9])", " ", expression))
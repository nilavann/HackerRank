#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    #
    # Write your code here.
    #
    maxscore = minscore = score[0]
    ls = hs = 0
    for n in score:
        if maxscore < n:
            maxscore = n
            hs += 1
        if minscore > n:
            minscore = n
            ls += 1
    return hs, ls

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()

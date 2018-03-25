#!/bin/python3

set1, set2 = [set(input().split()) for _ in range(4)][1::2]
# print( "\n".join(sorted(set1.symmetric_difference(set2), key = int)))
print( "\n".join(sorted(set1^set2, key = int)))
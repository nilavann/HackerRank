#!/bin/python3

import sys
# create a string with given two characters and check they are consequtive
def createString(s, char1, char2):
    newString = "".join( [ char for char in s if( char == char1 or char == char2)])
    for i in range( len(newString) - 1):
        if( newString[i] == newString[i + 1]):
            return ""
    else:
        return newString

def twoCharaters(s):
    # Complete this function
    unique = list(set(s))
    
    result = [ len(createString(s,unique[i],j)) for i in range(len(unique)) \
              for j in unique[:i]+unique[i+1:]]
    return 0 if not result else max( result)
if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)

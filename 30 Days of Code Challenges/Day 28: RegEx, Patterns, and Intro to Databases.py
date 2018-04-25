#!/bin/python3

import sys
import re


N = int(input().strip())
l = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if( bool(re.match( r"^[a-z.]+@gmail\.com$", emailID))):
        l.append(firstName)
print( *sorted(l),sep="\n")
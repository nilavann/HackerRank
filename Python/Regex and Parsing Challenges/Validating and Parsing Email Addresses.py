#!/bin/python3

import re,email.utils

for _ in range( int( input())):
    userDetails = email.utils.parseaddr( input())
    if( re.match( r"^[a-z][\w\-.]*@[a-z]+\.[a-z]{1,3}$", userDetails[1])):
        print( email.utils.formataddr( userDetails))
    
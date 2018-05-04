#!/bin/python3
import re

words = ""
substring = []
for _ in range(int ( input())):
    words = words + input() + " "
for _ in range(int ( input())):
    print( len( re.findall( "\B" + input() + "\B", words)))
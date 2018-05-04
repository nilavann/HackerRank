#!/bin/python3

import re
import sys
sourceCode = sys.stdin.read()
comments = re.findall( r"(/\*.*?\*/|//.*?(?=\n))", sourceCode, re.DOTALL)
# since there no need of space at start of multiple comment 
print( *[ re.sub( "\n\s+", "\n",comment) for comment in comments], sep = "\n")
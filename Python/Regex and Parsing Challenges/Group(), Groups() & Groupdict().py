#!/bin/python3

import re

m = re.search( r"([a-zA-Z0-9])\1+", input())
print( m.group(1) if( m) else -1)
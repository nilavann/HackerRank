#!/bin/python3

import re

s = "[qwrtypsdfghjklzxcvbnm]"
# ?<= lookahead
m = re.findall( r"(?<="+s+")([aeiou]{2,})"+s, input(), re.I)

print( "\n".join(m or ['-1']))


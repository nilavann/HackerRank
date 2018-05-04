#!/bin/python3

import re

htmlMarkup = "\n".join( [ input() for _ in range( int( input()))])
domainName = re.findall( r"https?://(?:www2?.)?((?:[a-zA-Z0-9-]+\.){1,}(?:[a-zA-Z]+))", htmlMarkup)
print( ";".join( sorted( set( domainName))))
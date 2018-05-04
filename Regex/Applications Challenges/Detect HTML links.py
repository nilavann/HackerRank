#!/bin/python3
import re

regex = r'<a href="(.*?)".*?>([\w\s.,-/]*)(?=</)'
for _ in range( int( input())):
    htmlElement = input()
    result = re.findall( regex, htmlElement)
    for link, text in result:
        print( "{},{}".format( link,text.strip()))
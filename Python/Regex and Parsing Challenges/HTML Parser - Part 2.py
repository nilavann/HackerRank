#!/bin/python3

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment( self, data):
        numLines = len( data.split( "\n"))
        if( numLines > 1):
            print( ">>> Multi-line Comment", data, sep = "\n")
        else:
            print( ">>> Single-line Comment", data, sep = "\n")
    def handle_data( self, data):
        if data.strip():
            print( ">>> Data", data, sep = "\n")

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
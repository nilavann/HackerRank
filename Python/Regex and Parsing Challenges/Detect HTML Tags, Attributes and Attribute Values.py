#!/bin/python3

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print( tag)
        for attr in attrs:
            print( "->", attr[0], ">", attr[1])
    def handle_startendtag(self, tag, attrs):
        print( tag)
        for attr in attrs:
            print( "->", attr[0], ">", attr[1])

parser = MyParser()
parser.feed( "\n".join( [ input() for _ in range( int( input()))]))
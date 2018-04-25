#!/bin/python3

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print( "Start :", tag)
        for attr in attrs:
            print( "->", attr[0], ">", attr[1])
    def handle_startendtag(self, tag, attrs):
        print( "Empty :", tag)
        for attr in attrs:
            print( "->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print( "End   :", tag)

parser = MyParser()
parser.feed( "\n".join( [ input() for _ in range( int( input()))]))
#!/bin/python3

import re, sys

sourceCode = sys.stdin.read()
checkJava = re.compile( r"import java\.")
checkC = re.compile( r"#include<stdio.h>")
if( bool( re.search( checkJava, sourceCode))):
    print( "Java")
elif( bool( re.search( checkC, sourceCode))):
    print( "C")
else:
    print( "Python")
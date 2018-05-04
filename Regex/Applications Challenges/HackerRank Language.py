#!/bin/python3

import re

Regex = r"^(BASH|BRAINFUCK|C(LISP|LOJURE|PP|SHARP)?|D(ART)?|ERLANG|GO|GROOVY|HASKELL|JAVA(SCRIPT)?|LUA|OBJECTIVEC|OCAML|PASCAL|PERL|PHP|PYTHON|R(UBY)?|SBCL|SCALA)$"
for _ in range( int( input())):
    print( "VALID" if( bool( re.match( Regex, input().split()[1]))) else "INVALID")
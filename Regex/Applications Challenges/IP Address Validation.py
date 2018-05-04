#!/bin/python3

import re

RegexForIpv4 = r"^((1[0-9]{2}|2[0-4][0-9]|25[0-5]|[0-9][0-9]?)\.){3}(1[0-9]{2}|2[0-4][0-9]|25[0-5]|[0-9][0-9]?)$"
RegexForIpv6 = r"^([a-f\d]{1,4}:){7}[a-f\d]{1,4}$"
for _ in range( int( input())):
    Ipaddress = input()
    if( bool( re.match( RegexForIpv4,Ipaddress))):
        print( "IPv4")
    elif( bool( re.match( RegexForIpv6,Ipaddress))):
        print( "IPv6")
    else:
        print( "Neither")
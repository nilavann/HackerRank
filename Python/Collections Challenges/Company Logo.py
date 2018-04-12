#!/bin/python3

import sys
from collections import OrderedDict, Counter

class OrderedCounter( Counter, OrderedDict):
    pass
[ print( *d) for d in OrderedCounter( sorted(input())).most_common(3)]

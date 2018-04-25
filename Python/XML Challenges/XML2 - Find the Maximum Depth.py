maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if( level >= 0 and maxdepth == level):
        maxdepth = level + 1
    # print( elem, level)
    for child in elem:
        depth(child, level+1)


def average(array):
    # your code goes here
    distinctHeights = set(array)
    return sum(distinctHeights) / len(distinctHeights)
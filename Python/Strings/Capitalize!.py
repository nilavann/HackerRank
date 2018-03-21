def capitalize(string):
    words = string.split(" ")
    return ' '.join([ word.capitalize() for word in words])
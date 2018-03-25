def print_rangoli(size):
    # your code goes here
    import string
    lowerCaseAlphabet = string.ascii_lowercase
    output = []
    for i in range(size):
        letters = "-".join(lowerCaseAlphabet[i:size])
        output.append(((letters[::-1]+letters[1:]).center((size + ((size - 1) * 3)),"-")))
    print("\n".join(output[::-1]+output[1:]))
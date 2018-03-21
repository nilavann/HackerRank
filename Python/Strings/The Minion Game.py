def minion_game(string):
    # your code goes here
    vowel  = "AEIOU"
    Stuart = 0
    Kevin = 0
    for i,c in enumerate(string):
        if c in vowel:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    if( Kevin == Stuart):
        print( "Draw")
    elif( Kevin > Stuart):
        print( "Kevin",Kevin)
    else:
        print( "Stuart",Stuart)
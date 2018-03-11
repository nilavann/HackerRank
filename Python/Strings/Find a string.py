def count_substring(string, sub_string):

    '''

    # method 1
    count = 0
    while( string.find(sub_string) != -1):
        count += 1
        string = string[string.find(sub_string)+1:]
    return count
    '''
    # method 2
    return sum( [1 for i in range( len( string) - len( sub_string) + 1) if string[i:i + len( sub_string)] == sub_string])
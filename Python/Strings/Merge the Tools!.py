def merge_the_tools(string, k):
    # your code goes here
    t = [string[i:i + k] for i in range(0,len(string),k)]
    for w in t:
        u = []
        for c in w:
            if c not in u:
                u.append(c)
        print( ''.join(u))
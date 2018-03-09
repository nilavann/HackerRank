if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        given = input().split()
        if given[0] == "print":
            print (arr)
        else:
            eval("arr."+given[0] + '(' + ",".join(given[1:]) + ")")
        

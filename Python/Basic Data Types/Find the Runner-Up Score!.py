if __name__ == '__main__':
    n = int(input())
    '''
    # method 1
    arr = list(map(int, input().split()))
    runner = min(arr)
    for i in arr:
        if( ( i < max( arr)) and ( i > runner)):
            runner = i
    print( runner)
    '''
    
    # method 2
    
    arr = sorted(set(map(int, input().split())))
    print( arr[ -2])
    
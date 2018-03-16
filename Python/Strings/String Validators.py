if __name__ == '__main__':
    s = input()
    
    # method 1
    for method in [str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]:
        for char in s:
            if( method( char)):
                print("True")
                break
        else:
            print("False")
            
    # method 2
    '''
    for method in [str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]:
        print( any( method(char) for char in s))
    '''
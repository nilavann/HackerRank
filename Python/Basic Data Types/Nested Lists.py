def second(element):
    return element[1]
if __name__ == '__main__':
    students = [ [ input(), float(input())] for _ in range( int( input()))]
    # secondHighest = 
    secondHighest = sorted(set([mark for name,mark in students]))[1]
    print( "\n".join( sorted( [ name for name,mark in students if ( mark == secondHighest)])))
#!/bin/python3
def wrapper(f):
    def fun(l):
        # complete the function
        return f( [ "+91 " + pnumber[-10:-5] + " " + pnumber[-5:] for pnumber in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
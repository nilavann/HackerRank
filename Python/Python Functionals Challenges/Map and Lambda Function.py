#!/bin/python3

cube = lambda x: pow( x, 3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    l = [0,1]
    a = 0
    b = 1
    for i in range(2,n):
        fib = a + b
        l.append( fib)
        a, b = b, fib
    return l[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
#!/bib/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = list(map(int, input().split()))
costs = list(map(int,input().strip().split()))
annaShare = int(input())

# calculating annaShare
'''
# method 1
equalShare = sum(costs[:k]+costs[k+1:])//2
'''

# method 2
equalShare = (sum(costs) - costs[k])//2

# print result using if else
print( annaShare - equalShare) if(equalShare != annaShare) else print("Bon Appetit")
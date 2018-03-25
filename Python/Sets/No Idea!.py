n, m  = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())

# print( sum((c in A) - (c in B) for c in array)) 

# print( sum( 1 for c in array  if(c in A)) + sum( -1 for c in array if(c in B)))

score = 0
for c in array:
    if(c in A):
        score += 1
    if(c in B):
        score += -1
print( score)
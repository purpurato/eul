"""
Problem 14
Longest Collatz sequence
"""

collength = []
for n in range(2,1000001):
    #print("Collatz %d:" % n)
    lis = [n]
    while n > 1:
        if n % 2 == 0:
            n /= 2
            lis.append(int(n))
        else:
            n = 3*n + 1
            lis.append(int(n))
    collength.append(len(lis))
    #print(lis)

ans = collength.index(max(collength))+2
print(ans)
# positional index in collength
# collength[0] = 2 

"""
Problem 40 Project 40
"""

nbr=''
for x in range(1000001):
    nbr += str(x)

rslt = 1
for x in range(7):
    rslt *= int(nbr[10**x])

print(rslt)

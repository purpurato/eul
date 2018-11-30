"""
Problem 36 Project Euler
find sum of all palindromic numbers in
decimal base and binary base
e.g 585 = 1001001001 both palindromes
Find the sum of all palindromics till 1 million
"""

dec = ''
bina = ''

palis = []


for x in range(1,1000001):
    dec = str(x)
    bina = bin(x)[2:]
    if dec == dec[::-1] and bina == bina[::-1]:
        palis.append(x)
sum(palis)

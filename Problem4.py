"""
Problem 4 Project Euler
Largest palindrome product
"""

import eulerfunctions
from itertools import combinations as comb

lis = [x for x in range(100,1000)]
combs = list(comb(lis,2))

lispal = []
for x in range(len(combs)):
        a = combs[x][0] * combs[x][1]    
        if eulerfunctions.ispalind(a):
                lispal.append(a)
                #print("%d x %d = %d" % (combs[x][0], combs[x][1], a))

print("The largest palindrome product\
 of 2 digit numbers is %d" % (max(lispal)))

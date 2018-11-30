"""
Problem 44 Project Euler
Pentagon numbers
"""

# Pentagon numbers increase in a quadratic function
# so the difference between them increase too.

import itertools
#import pdb

#pdb.set_trace()

pents = [int(n*(3*n-1)/2) for n in range(1,1001)]
couples = list(itertools.combinations(pents,2))

lis = []
for x in range(1000):
    a = pents[x]
    for y in range(x+1, 1000):
        b = pents[y]
        pensum = a+b
        pendif = abs(a-b)
        if pensum in pents and pendif in pents:
            print(a, b)

"""
Problem 39 Project Euler
Integer right triangles
"""

#square of integers are below 1000 for int's below 31
# 31**2 = 961 and 32**2 = 1024
from math import sqrt as sqrt
import collections
solutions = set()

for a in range(1,1998):
    for b in range(1,1998):
        c = sqrt(a**2 + b**2)
        if (a+b+c) <= 1000 and int(c) == c:
            sides = sorted([a,b,c])
            sides = tuple(sides)
            solutions.add(sides)

perims = [sum(x) for x in solutions]
counter = collections.Counter(perims)

for key, value in counter.items():
    print(key, value)

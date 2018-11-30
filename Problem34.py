"""
Problem 34 Project Euler
Numbers for which the sum of the factorial of
its digits is equal to number itself.
e.g. 1! + 4! + 5! = 145
"""
import timeit
from math import factorial as f

start_time = timeit.default_timer()
lis = []

for x in range(100000):
    sf = 0
    a = str(x)
    for y in a:
        y = f(int(y))     
        sf += y
    if sf == x:
        lis.append(sf)

print(sum(lis))
elapsed = timeit.default_timer() - start_time
print(elapsed)

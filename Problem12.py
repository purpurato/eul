"""
Problem 12  
Highly divisible triangular number
"""

import timeit
from sympy import divisor_count

start_time = timeit.default_timer()

tr = 0 
for x in range(1,100000):
    tr += x
    if divisor_count(tr) > 500:
        print(tr)
        break

elapsed = timeit.default_timer() - start_time
print("Execution time: %.3f s" %elapsed)  

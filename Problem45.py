"""
Problem 45 Project Euler
Triangular, pentagonal and hexagonal
"""
import timeit

start_time = timeit.default_timer()

triangs = [n*(n+1)/2 for n in range(1,100000)]
pentags = [n*(3*n-1)/2 for n in range(1,100000)]
hexags = [n*(2*n-1) for n in range(1,100000)]

for x in triangs:
    if x in pentags and x in hexags:
        print(x)
        
elapsed = timeit.default_timer() - start_time
print(elapsed)

# run time 150s how to optimize?

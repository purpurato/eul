"""
Problem 10
Summation of primes
"""

from sympy import sieve

lis = [x for x in sieve.primerange(0,2000000)]
print(sum(lis))

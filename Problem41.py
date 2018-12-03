"""
Project Euler 
Problem  41 - Pandigital prime
"""

from itertools import permutations
from sympy.ntheory import isprime

# Finds permutations of largest 9 digit pandigital numbers
larg_pandig_9 = list(permutations('123456789',9))
# Search was done manually for pandigitals of 8 and 7 digits
larg_pandig_8 = list(permutations('12345678',8))
larg_pandig_7 = list(permutations('1234567',7))

def tup_to_int(x):
    """Takes a tuple with chr and returns an int"""
    num = ''
    for a in x:
        num += a
    return int(num)

larg_pandig_7 = [tup_to_int(x) for x in larg_pandig_7]
larg_pandig_7.sort(reverse=True)

for x in larg_pandig_7:
    if isprime(x):
        print(x)
        break


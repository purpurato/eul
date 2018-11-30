"""
Problem 3 Largest prime factor
"""
import math
import pdb

primes = [2,3,5]

number = int(input("Find all primes up to: "))

pdb.set_trace()
# Finds all primes up to number
for x in range(6,math.ceil(math.sqrt(number))):
    count = 0
    for y in primes:
        if x % y != 0:
            count += 1
    if count == len(primes):
        primes.append(x)

print(primes)

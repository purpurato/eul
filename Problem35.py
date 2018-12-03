"""
Project Euler 
Problem  35 - Circular primes
"""

from sympy.ntheory import isprime

def rotations(x):
    """Takes a number and returns its rotations
    as a list"""
    x = list(str(x))
    rottns_lis = []
    for a in range(len(x)):
        rottns_lis.append(x[a:] + x[:a])
    
    rottns_num = [int(''.join(a)) for a in rottns_lis]
    return rottns_num
    
circul_primes = []
for x in range(1,1000000):
    testlis = []
    if isprime(x):
        testlis = [isprime(a) for a in rotations(x)]
        if all(testlis):
            circul_primes.append(x)
        
print(len(circul_primes))

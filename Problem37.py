"""
Project Euler 
Problem 37 - Truncatable primes
"""

from sympy.ntheory import isprime

def truncat(x):
    """Returns a list of truncates of a number"""
    x = str(x)

    truncs = []
    for a in range(1,len(x)):
        truncs.append(x[:a])
        truncs.append(x[a:])
    
    truncs = [int(x) for x in truncs]
    return truncs

primes = []
coun = 1
while len(primes) < 15:
    trunc_primes = []
    if isprime(coun):
        trunc_primes = [isprime(x) for x in truncat(coun)]
        
        if all(trunc_primes):
            primes.append(coun)
    
    coun += 1

primes = primes[4:]
print(primes)
print(sum(primes))

"""
Project Euler 
Problem  27 - Quadratic primes 
"""

from sympy.ntheory import isprime

eulerformula = [n**2 + n + 41 for n in range(40)]

def lisprime(lis):
    """Checks if numbers in list are all primes"""
    checklis = []
    for x in lis:
        if isprime(x):
            checklis.append(True)
    if all(checklis):
        return True
    else:
        return False
        

lis_coefs = {}
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        lisprimes = []
        
        for n in range(5000):
            prim = n**2 + a*n + b
            if isprime(prim):
                lisprimes.append(prim)
            else:
                lis_coefs[len(lisprimes)] = [a,b]
                break
 
#print(lis_coefs)
maxprimes = [] 
for key, values in lis_coefs.items():
    maxprimes.append(key)
    
maxprimes.sort()
print("The largest number of primes with formula is {}".format(maxprimes[-1]))
a = maxprimes[-1]
print('Coefficienta a is {} and b {}'.format(lis_coefs[a][0],lis_coefs[a][1]))
print('The product a*b is {}'.format(lis_coefs[a][0]*lis_coefs[a][1]))

    

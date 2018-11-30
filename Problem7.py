"""
Problem 7 Project Euler 
finds the n'th prime number 
"""

#import pdb
#pdb.set_trace()
primes = [2]
number = 3
a = input("Enter the n'th prime number to be found: ")
a = int(a)

while len(primes) < a:  
    cter = []
    sqr = int(number**0.5)
    
    for y in primes:
        if y <= sqr:
            cter.append(number%y)
        else:
            break
    if cter.count(0) == 0:
        primes.append(number)
    number += 1

#print(primes)
print(primes[-1])

"""
Problem 53 Project Euler 
Combinatoric selections
"""
from math import factorial as fact

def C(n,r):
    """This function gives the number of r combinations of n set"""
    combs = int(fact(n)/(fact(r)*fact(n-r)))
    return combs

count = 0
for n in range(100,1,-1):
    for r in range(2,n-1):
        if C(n,r) > 1000000:
            #this print shows all the combinations 
            #print('C(%d,%d) = %d' % (n, r, C(n,r)))
            count += 1
            
print("For n up to 100, there are %d combinations higher than\
 one million" % count)


  

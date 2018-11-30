"""
Problem 52 Project Euler
Permuted multiples
"""

for x in range(1,1000000):
    doub = sorted(list(str(2*x)))
    trip = sorted(list(str(3*x)))
    quad = sorted(list(str(4*x)))
    quin = sorted(list(str(5*x)))
    sext = sorted(list(str(6*x)))

    if doub == trip == quad == quin == sext:
        print(x)
        
    
    

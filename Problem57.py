"""
Problem 57
Square root convergence
"""

from sympy import cancel

nth = int(input("Enter which expansion: "))

a0 = '1 + 1/2'
count = 0

for x in range(nth-1):
    an = '1 + 1/(1 + (a0))'
    an = an.replace('a0', a0)
    an= str(cancel(an))
    a0 = an
    
    an = an.split('/')
    numerat = an[0]
    denomin = an[1]
    
    if len(numerat) > len(denomin):
        count += 1

print("In the nth expansion there are")
print(count)
print("expressions with numerators with more numbers than denominators")

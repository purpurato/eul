"""
Project Euler
Problem 33 - Digit cancelling fractions
"""

from sympy import cancel

count = 0
numerators, denominators = [],[]
for numer in range(10,100):
    for denom in range(numer+1,100):
        str_numer = str(numer)
        str_denom = str(denom)
        expr = str_numer + '/' + str_denom
        expr = str(cancel(expr))
        
        
        if str_numer[0] in str_denom[0]:
            frac = str_numer[1] + '/' + str_denom[1]
            frac = str(cancel(frac))
            if expr == frac:
                print('{}/{}'.format(numer,denom))
                numerators.append(numer)
                denominators.append(denom)
            
        if str_numer[0] in str_denom[1]:
            frac = str_numer[1] + '/' + str_denom[0]
            frac = str(cancel(frac))
            if expr == frac:
                print('{}/{}'.format(numer,denom))
                numerators.append(numer)
                denominators.append(denom)
        
        if str_numer[1] in str_denom[0]:
            frac = str_numer[0] + '/' + str_denom[1]
            frac = str(cancel(frac))
            if expr == frac:
                print('{}/{}'.format(numer,denom))
                numerators.append(numer)
                denominators.append(denom)

#print('Numerators {}'.format(numerators))
#print('Denominators {}'.format(denominators))

prod_numer, prod_denom = 1,1
for x in numerators:
    prod_numer *= x

for x in denominators:
    prod_denom *= x

print('Product of fractions on lowest common terms')
print(cancel(str(prod_numer) + '/' + str(prod_denom)))

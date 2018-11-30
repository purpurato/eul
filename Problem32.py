"""
Project Euler
Problem 32 - Pandigital products 
"""

import itertools 
#import pdb

permlis = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

# sum to be found
sumtot = 0  

def ispandit(exp1, exp2):
    """Evaluates if two expressions are equal 
    and prints them"""
    if eval(exp1) == eval(exp2):
        print("%s = %s" % (exp1, exp2))
        return True
    else:
        return False
    
for ind, x in enumerate(permlis):     
    a = str(permlis[ind][0])
    b = str(permlis[ind][1])
    c = str(permlis[ind][2])
    d = str(permlis[ind][3])
    e = str(permlis[ind][4])
    f = str(permlis[ind][5])
    g = str(permlis[ind][6])
    h = str(permlis[ind][7])
    i = str(permlis[ind][8])
    
    # Possibilities for the product
    # with 2 and 3 digits factors and 4 dig result
    # e.g 39 × 186 = 7254 noted as 2-3-4
    # note case 2-3-4 and 3-2-4 are the same

    # case 1-4-4
    exp1 = a + '*' + b+c+d+e
    exp2 = f+g+h+i
    if ispandit(exp1,exp2):
        sumtot += int(exp2)
    
    # case 2-3-4
    exp1 = a+b + '*' + c+d+e
    exp2 = f+g+h+i
    if ispandit(exp1,exp2):
        sumtot += int(exp2)
        
    # case 3-3-3
    exp1 = a+b+c + '*' +d+e+f
    exp2 = g+h+i
    if ispandit(exp1,exp2):
        sumtot += int(exp2)
    
print("The sum for all cases is: %d" % sumtot)

 

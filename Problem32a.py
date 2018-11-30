"""
Problem 32 Project Euler
find sum of all pandigital products from 1 to 9
e.g 39 × 186 = 7254
There are 9! = 362880 possibilities
"""

from itertools import permutations as perm
import pdb

permlis = list(perm([1,2,3,4,5,6,7,8,9,'==','*']))

pdb.set_trace()   
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
    j = str(permlis[ind][9])
    k = str(permlis[ind][10])

    expr = a+b+c+d+e+f+g+h+i+j+k

    if eval(expr):
            print(expr)
            


    
    

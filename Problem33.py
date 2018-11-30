"""
Problem 33 Project Euler
"""

import pdb 
from itertools import combinations as comb

nums = [x for x in range(10,100)]

combis = list(comb(nums,2))

pdb.set_trace()
for ind, x in enumerate(combis):
    num = list(str(x[0]))
    den = list(str(x[1]))
    
    for a in num:
        if a in den:
            print('%s/%s' % (str(x[0]), str(x[1])))
            num = num.remove(a)
            den = den.remove(a)
        print('%s/%s' % (num[0], den[0]))

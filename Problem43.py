"""
Problem 43 Project Euler
pandigital numbers
"""

from itertools import permutations as perm
import timeit

start_time = timeit.default_timer()

s = 0
for l in list(perm([0,1,2,3,4,5,6,7,8,9])):
    
    a = str(l[7]) + str(l[8]) + str(l[9])
    if int(a) % 17 !=0:
        continue

    a = str(l[6]) + str(l[7]) + str(l[8])
    if int(a) % 13 != 0:
        continue

    a = str(l[5]) + str(l[6]) + str(l[7])
    if int(a) % 11 != 0:
        continue

    a = str(l[4]) + str(l[5]) + str(l[6])
    if int(a) % 7 != 0:
        continue

    a = str(l[3]) + str(l[4]) + str(l[5])
    if int(a) % 5 != 0:
        continue

    a = str(l[2]) + str(l[3]) + str(l[4])
    if int(a) % 3 != 0:
        continue

    a = str(l[1]) + str(l[2]) + str(l[3])
    if int(a) % 2 != 0:
        continue 

    n = ''
    for x in l:
        n += str(x)

    s += int(n)
    
print(s)

elapsed = timeit.default_timer() - start_time
print("Run time: %.2f s" % elapsed)

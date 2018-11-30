"""
Project Euler 
Problem  62 - Cubic permutations
"""
from collections import Counter

def ispermut(a, b):
    a, b = str(a), str(b)
    if Counter(a) == Counter(b):
        return True
    else:
        return False

# Five digits cubes start at 22**3 == 10648
cubes = [x**3 for x in range(22,10001)]

# Search in all cubes
for index, x in enumerate(cubes):
    perms = []
    # For each search, start only at last value analysed
    for y in cubes[index+1:]:
        # Analyse only numbers with same number of digits
        if len(str(y)) > len(str(x)):    
            break
        else:
            if ispermut(x, y):
                perms.append(y)
                perms.append(x)
        
    if len(set(perms)) == 5:
        permset = set(perms)
        print(permset)
        break


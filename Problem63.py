"""
Project Euler 
Problem  63 - Powerful digit counts
"""

# Search only through one digit numbers (1-9)
# cause 10**2 = 100 (3 digits). 
# And the largest power of 9 is 23

digits = [x for x in range(1,10)]
powers = [x for x in range(1,24)]

coun = 0
for a in digits:
    for n in powers:
        resul = a**n
        if len(str(resul)) == n:
            coun += 1
print(coun)

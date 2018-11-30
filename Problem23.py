"""
Project Euler 
Problem  23 - Non-abundant sums
"""

from sympy import divisors

def isabundant(x):
    """Defines if a number is abundant"""
    if sum(divisors(x)[:-1]) > x:
        return True
    else:
        return False

# Finds all the abundant numbers up to 28123
abunds = []
for x in range(1,28123):
    if isabundant(x):
        abunds.append(x)
print(abunds)
# There are 6965 abudant numbers up to 28123

ints = []
for x in range(1,28123):
    if x < 24:
        ints.append(x)
    

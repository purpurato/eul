"""
Problem 21 Project Euler
Amicable numbers
"""

def divisors(x):
    divs = []
    for i in range(1,x):
        if x % i == 0:
            divs.append(i)
    
    return sum(divs)

def hasamicable(a):
    b = divisors(a)
    if divisors(b) == a and a != b:
        return sorted([a, b])
    else:
        return False

amicables = set()
for x in range(1,10001):
    if hasamicable(x):
        amicables.add(x)
        
print(amicables)
print(sum(amicables))

"""
Problem 30 Project Euler
find number that is equal to the 5th power sum of its digits
e.g xyz = x**5 + y**5 + z**5
"""

lis= []
for x in range(100000):
    y = str(x)
    digsum = 0

    for z in y:
        digsum += int(z)**5

    if digsum == x:
        lis.append(x)
        
# testing with x up to 1 million

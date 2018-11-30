"""
Problem 29 Project Euler
Distinct powers
"""

a = input("Enter a: ")
b = input("Enter b: ")
a, b = int(a), int(b)
lis = []

for x in range(a,b+1):
    for y in range(a,b+1):
        dispow = x**y
        #print("%d**%d = %d" % (x,y,dispow))
        if dispow not in lis:
            lis.append(dispow)

lis.sort()
#print("Distinct powers are: ")
#print(lis)
print("There are %d elements" % len(lis))

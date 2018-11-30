"""
Problem 6 
Sum square difference
""" 

lissq = []
sqlis = []

for a in range(1,101):
    lissq.append(a**2)
    sqlis.append(a)

print(sum(sqlis)**2-sum(lissq))


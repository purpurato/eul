"""
Problem 25 Project Euler
"""

a = 0
b = 1
c = a + b
fibs = [1]

for x in range(4900):
    #print('F' + str(x+1) + ' = ' + str(b))
    #print('%s digits' %len(str(b)))
    a = b
    b = c
    c = a + b
  
    
    if len(str(b)) == 1000:
        print('F' + str(x+1) + ' = ' + str(b))
        print('%s digits' %len(str(b)))

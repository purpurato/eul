"""
Problem 28 Project Euler
Numbers spiral 
"""  

import numpy as np
import pdb

# Four directions in order: right, down, left, up.

count = 1       # value in array 
arrs = input("Input array size (only odd nbrs): ")
arrs = int(arrs)
cent = int((arrs-1)/2)

arr = np.array([[0]*arrs]*arrs)
arr[cent][cent] = 1

#pdb.set_trace()

# insert a try block to handle IndexError
for x in range(1,len(arr)+1):
    try:    
        if x % 2 != 0:
            ind = int((x+1)/2)      
            for y in range(x):
                count += 1                  
                arr[cent+1-ind][cent+2-ind+y] = count       # right    
            for y in range(x):
                count += 1
                arr[cent+2+y-ind][ind+cent] = count         # down
     
        else:
            ind = int(x/2)
            for y in range(x):
                count += 1               
                arr[cent+ind][cent-1+ind-y] = count         # left  
            for y in range(x):
                count += 1
                arr[cent-1+ind-y][cent-ind] = count         # up    
    except:
        break

print(arr)
    
s = 0
for x in range(len(arr)):
    #print("%d %d" % (arr[x][x], arr[x][len(arr)-1-x]))
    s += arr[x][x] + arr[x][len(arr)-1-x] 

print("The sum in diagonal is: %d" % (s-1))

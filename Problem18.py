"""
Maximum path sum I
Problem 18 Project Euler 
"""

#import numpy as np

# triangle as copied from website
tr = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

tr = tr.split('\n')
tr = [x.split(' ') for x in tr]

for row, x in enumerate(tr):
	for col, y in enumerate(x):
		tr[row][col] = int(tr[row][col])

#tr = np.array(tr)
#In each row the path chosen leads to the loss of a complete 
#'column' on the opposite side that is not reachable
new_pyramid = tr
# Sum value initialized
s = 75
for row in range(14):
    right_pyramid = []
    left_pyramid = []
    for x in range(14-row):
        right_pyramid.append(new_pyramid[x+1][1:])
        left_pyramid.append(new_pyramid[x+1][:-1])

    sumright, sumleft = 0,0
    
#    for x in right_pyramid:
#        sumright += sum(x)
    for x in new_pyramid:
        sumright += x[-1]
        sumleft += x[0]
    
#    for x in left_pyramid:
#        sumleft += sum(x)

    if sumright > sumleft:
        new_pyramid = right_pyramid
        s += new_pyramid[0][0]
        print(new_pyramid[0][0], end=' ')
        print(s)
   
    else:
        new_pyramid = left_pyramid
        s += new_pyramid[0][0]
        print(new_pyramid[0][0], end=' ')
        print(s)


#Getting the sums of the pyramids on each side and 
#choosing the largest R/883

#Getting the sums of the columns 
#choosing the shortest R/

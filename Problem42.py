"""
Problem 42 Project Euler
Coded triange numbers
"""

import csv

tr = []
for n in range(1,50):
    seq = int(0.5*n*(n+1))
    tr.append(seq)

s = 0

# function to convert words to sum of ordinals of its letters
def trtest(s):
    su = 0 
    for x in s:
        su += ord(x) - 64
    return su

nbtr = 0
with open('words.txt') as fob:
    reader = csv.reader(fob)

    for x in reader:
        for y in x:
            res = trtest(y)

            if res in tr:
                nbtr += 1
                #print(y)
                #print(trtest(y))

print(nbtr)

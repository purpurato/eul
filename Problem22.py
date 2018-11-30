"""
Problem 22
Project Euler
"""
import timeit

start_time = timeit.default_timer()

nams = []
with open('names.txt','r') as fp:
    for x in fp:
        nams.append(x)

nams = nams[0].split(',')
nams = [x.replace('"','') for x in nams]
nams.sort()

def charval(x):
    """Takes a word and sums the value of the letters
    e.g. COLIN => 3+15+... = 53"""
    chars = [ord(a)-64 for a in x]
    return sum(chars)
    
s = 0
for index, n in enumerate(nams):
    s += (index+1) * charval(n)
    
print(s)

elapsed = timeit.default_timer() - start_time
print("Execution time: %.3f s" %elapsed)

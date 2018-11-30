"""
Project Euler 
Problem  61 - Cyclical figurate numbers
"""

def polygo(p,n):
    """Function generates polygonal numbers
    given 'sides' and set as arguments"""
    if p == 3:
        return int(n*(n+1)/2)
    elif p == 4:
        return int(n**2)
    elif p == 5:
        return int(n*(3*n-1)/2)
    elif p == 6:
        return int(n*(2*n-1))
    elif p == 7:
        return int(n*(5*n-3)/2)
    elif p == 8:
        return int(n*(3*n-2))

#set with 4 digits are range:
triangs = [polygo(3,n) for n in range(45,141)]
squars = [polygo(4,n) for n in range(32,100)]
pents = [polygo(5,n) for n in range(26,82)]
hexs = [polygo(6,n) for n in range(23,71)]
hepts = [polygo(7,n) for n in range(21,64)]
octs = [polygo(8,n) for n in range(19,59)]

all_cycl = [triangs,squars,pents,hexs,hepts,octs]

def arecycl(a,b,c,d,e,f):
    """Finds if all six arguments are cyclical numbers"""
    a,b,c,d,e,f = str(a),str(b),str(c),str(d),\
    str(e),str(f)
    lis = [a,b,c,d,e,f]
    
    first = lis.pop(0)
    for x in range(5):
        count_y = 0
        for index, y in enumerate(lis):
            if first[-2:] == y[:2]:
                first += lis.pop(index)
                count_y += 1
                continue
        if count_y == 0:
            break
    
    if first[-2:] == first[:2] and len(first) == 24:
        return True
    else:
        return False
    

#print(arecycl(7284,4572,8435,3579,7964,6445))
#print(arecycl(6572,7284,8435,3579,7964,6445))

#class SearchTree():
#    """"Search for trees in each """
#    
#    def __init__(self, octa):
#        self.octa = octa
#    
#    def link_nod(self

trees = []
for a in octs:
    first = a[-2:]
    for b in hepts:
        if b[:2] == first:
            trees.append(b)
    
    

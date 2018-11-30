"""
Problem 31 
Coin sums
"""
#import pdb

coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
# Factors to multiply each type of coin
# e.g 1 for 2 coins and 2 for 1 coins

def testexpr(a,b,c,d,e,f,g,h):
    expr = a*2 + b + c*0.5 + d*0.2 + e*0.1 + \
    f*0.05  + g*0.02 + h*0.01
    if expr >= 0:
        return False

count = 0
a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0
for a in range(1,-1,-1):
    if testexpr(a,b,c,d,e,f,g,h):
        break
    for b in range(2,-1,-1):
        if testexpr(a,b,c,d,e,f,g,h):
            break
        for c in range(5,-1,-1):
            if testexpr(a,b,c,d,e,f,g,h):
                break
            for d in range(10,-1,-1):
                if testexpr(a,b,c,d,e,f,g,h):
                    break
                for e in range(20,-1,-1):
                    if testexpr(a,b,c,d,e,f,g,h):
                        break
                    for f in range(40,-1,-1):
                        if testexpr(a,b,c,d,e,f,g,h):
                            break
                        for g in range(100,-1,-1):
                            if testexpr(a,b,c,d,e,f,g,h):
                                break
                            for h in range(200,-1,-1):
                                if testexpr(a,b,c,d,e,f,g,h):
                                    break
                                if a*2 + b + c*0.5 + d*0.2 + \
                                e*0.1 + f*0.05  + g*0.02 \
                                + h*0.01 == 2:  
                                #print(a,b,c,d,e,f,g)
                                    count += 1
    
print(count)

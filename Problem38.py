"""
Problem 38
Largest concatenated product
"""

def ispandigit(x):
        """Evaluates if argument (str) is pandigit
from 1 to 9."""
        x = list(x)
        x.sort()
        digits  = [str(x) for x in range(1,10)]
        if digits == x:
                return True
        else:
                return False
        
for x in range (1,100000):
        conc = ''
        for y in range(1,10):   	        # numbers that multiply    
                prod = x*y                      # assumes no larger than 9
                conc += str(prod)
                if ispandigit(conc):
                        print(conc, x)

# Last number printed is the largest pandigit

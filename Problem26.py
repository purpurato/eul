"""
Problem 26 Project Euler
Reciprocal cycles 
"""

from decimal import Decimal

nums = []
for x in range(1,101):
    a = str(Decimal(1/x))
    print(a[2:])
    
    

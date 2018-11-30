"""
Project Euler 
Problem  35 - Circular primes
"""

def rotations(x):
    """Takes a number and returns its rotations
    as a list"""
    x = str(x)
    rottns = []
    for a in range(len(x)):
        x[-1] = x[0]
        for b in range(

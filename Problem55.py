"""
Problem 55 Euler Project
Lychrel numbers 
"""

def ispalind(num):
        """Test if number is palindrome."""
        num = list(str(num))
        if num == num[::-1]:
                return True

def reverse(num):
    num = str(num)[::-1]
    return int(num)

lychrells = 0   
for x in range(1,10001):
    iter = 0 
    resul = x
    for y in range(50):        
#        print('{} + {} = {}'.\
#        format(resul, reverse(resul), resul+reverse(resul)))
        resul = resul + reverse(resul)
        iter += 1
        
        if ispalind(resul):
            #print(x)
            #print('{} iterations'.format(iter))
            break
        if iter == 50:
            #print('{} is Lychrell'.format(x))
            lychrells += 1

print('There are {} Lychrell numbers below 10000'.format(lychrells))

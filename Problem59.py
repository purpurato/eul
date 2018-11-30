"""
Project Euler
Problem 59 - XOR decryption
"""


# key is 3 lower case characters 
# that is ASCII from 97 to 122

ciphertext = ''
with open('cipher.txt') as fp:
    ciphertext= fp.read()

ciphertext = ciphertext.split(',')
ciphertext = [int(x) for x in ciphertext]

def decip(a,b,c,ciphertext):
    """Writes a text using a,b,c as keys and ciph as 
    cipher text """
    decip = ''
    try:
        for x in range(0,len(ciphertext),3):
            decip += chr(ciphertext[x] ^ ord(a))
            decip += chr(ciphertext[x+1] ^ ord(b))
            decip += chr(ciphertext[x+2] ^ ord(c))
    except IndexError:
        pass
    return decip
    
# Search of all possible combinations of keys with lower
# case alphabet letters appended to possib_keys
# and deciphered text appended to possibs
possibs = []
possib_key = []
for x in range(97,123):
    for y in range(97,123):
        for z in range(97,123):
            possibs.append(decip(chr(x),chr(y),chr(z),ciphertext))
            k = [chr(x),chr(y),chr(z)]
            possib_key.append(k)

# The word 'the' is the most common in english 
count_the = []
for x in possibs:
    count_the.append(x.count('the'))

print("The index of text with highest amount of 'the' is")
print(count_the.index(max(count_the)))
print("The letters corresponding to that key are")
print(possib_key[4423])
print("Deciphered text is the following")
print(decip('g','o','d',ciphertext))

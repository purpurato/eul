"""
Nummber letter counts
Problem 17 Euler
"""

nums = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    18:'eighteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred',
    1000:'one thousand'
    }

def onedig(x):
    xst = str(x)
    return nums[x]              # one digits all in dictionary
        
def twodig(x):
    xst = str(x)
    name = ''
    if x in nums:
        name = nums[x]
    elif xst[0] == '1':
        name = nums[int(xst[1])] + 'teen'
    elif xst[0] == '2':
        name = 'twenty' + ' ' + nums[int(xst[1])]
    elif xst[0] == '3':
        name = 'thirty' + ' ' + nums[int(xst[1])]
    elif xst[0] == '4':
        name = 'forty' + ' ' + nums[int(xst[1])]
    elif xst[0] == '5':
        name = 'fifty' + ' ' + nums[int(xst[1])]
    elif xst[0] == '6':
        name = 'sixty' + ' ' + nums[int(xst[1])]
    elif xst[0] == '7':
        name = 'seventy' + ' ' + nums[int(xst[1])]
    elif xst[0] == '8':
        name = 'eighty' + ' ' + nums[int(xst[1])]
    elif xst[0] == '9':
        name = 'ninety' + ' ' + nums[int(xst[1])]
    return name

def threedig(x):
    if x in nums:
        name = nums[x]
    xst = str(x)
    if xst[2] == '0' and xst[1] == '0':
        name = nums[int(xst[0])] + ' hundred' + twodig(int(xst[1:]))
    else:
        name = nums[int(xst[0])] + ' hundred and ' + twodig(int(xst[1:]))
    return name

"""
def fourdig(x):
    if x in nums:
        name = nums[x]
    xst = str(x)
    return nums[int(xst[0])] + ' thousand ' + threedig(int(xst[2:]))
"""

def numtolett(x):
    xst = str(x)
    if len(xst) == 1:
        name = onedig(x)
    elif len(xst) == 2:
        name = twodig(x)
    elif len(xst) == 3:
        name = threedig(x)
    else:
        name = 'one thousand'
    return name 

lis = ''
for x in range(1,1001):
    print(numtolett(x))
    lis += numtolett(x)

lis = lis.replace(' ','')
print(len(lis))

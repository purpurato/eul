"""
Problem 54 
Poker hands
"""
import collections

# Extract plays from poker.txt and adds it to 
# list 'plays'
plays = []
with open('poker.txt') as fp:
    for line in fp:
        plays.append(line)
        
plays = [x.replace('\n','') for x in plays]
plays = [x.split(' ') for x in plays]

# Splits each line two different plays 
play_one, play_two =[],[]
for x in plays:
    play_one.append(x[:5])
    play_two.append(x[5:])

card_order = ['2', '3','4', '5', '6', '7','8',\
'9','T', 'J', 'Q', 'K', 'A']
hand_order = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind',
'Straight', 'Full House', 'Four of a Kind','Flush', 'Straight Flush',
'Royal Flush']
# suits are Clovers, Diamonds, Hearts, Spades

def readhand(hand):
    """Takes a list and defines type of hand:
    Royal Flush, Straight Flush..."""
    nums = [x[0] for x in hand]
    nums = [card_order.index(x[0]) for x in hand]
    nums.sort()
    suits = [x[1] for x in hand]
    ch = [nums[x+1] - nums[x] for x in range(4)]
    
    
    if len(set(suits)) == 1:
        if 12 in nums and 11 in nums and 10 in nums \
        and 9 in nums and 8 in nums:
            return hand_order.index('Royal Flush')
        
        # J, Q, K, A, 2 can be straight flush?
        if all(x == 1 for x in ch):
            return hand_order.index('Straight Flush')
        
        else:
            return hand_order.index('Flush')
    
    if len(set(nums)) == 2:
        return hand_order.index('Four of a Kind')
    
    if nums[0] == nums[1] == nums[2] and \
    nums[3] == nums[4]:
        return hand_order.index('Full House')
    if nums[0] == nums[1] and \
    nums[2] == nums[3] == nums[4]:
        return hand_order.index('Full House')  
    
    # only works from 2 to K 
    # e.g not Q, K, A, 2, 3
    if all(x == 1 for x in ch):
        return hand_order.index('Straight')
    
    coun = [nums.count(x) for x in nums]
    if  3 in coun:
        return hand_order.index('Three of a Kind')
        
    if coun.count(2) == 4:
        return hand_order.index('Two Pairs')
    
    if coun.count(2) == 2:
        return hand_order.index('One Pair')
        
    return hand_order.index('High Card')

def evenhand(one, two):
    """Defines winner in case of same hand, 
    arguments are the two hands. Returns True
    for player one win."""
    nums_1 = [x[0] for x in one]
    nums_1 = [card_order.index(x[0]) for x in one]
    nums_1.sort()
    nums_2 = [x[0] for x in two]
    nums_2 = [card_order.index(x[0]) for x in two]
    nums_2.sort()
    
    # Even on High Card
    if readhand(one) == 0:
        hc1 = max(nums_1)
        hc2 = max(nums_2)
        if hc1 > hc2:
            return True
        else: 
            return False
    
    # Even on one pair, needs to decide 
    # if both pairs are the same !
    if readhand(one) == 1:
        for key, value in collections.Counter(nums_1).items():
            if value == 2:
                p1 = key
        
        for key, value in collections.Counter(nums_2).items():
            if value == 2:
                p2 = key
        
        if p1 > p2:
            return True
        elif p1 < p2:
            return False
            
        elif p1 == p2:
            h1, h2 = set(one), set(two)
            if max(h1) > max(h2):
                return True
            else:
                return False
        
 
play_one_wins = 0 
play_one_lose = 0
for x in range(1000):
#    print('{} - {}'.format(play_one[x], play_two[x]))
    if readhand(play_one[x]) > readhand(play_two[x]):
        play_one_wins += 1
#        print('Player one wins with {}'.format(hand_order[readhand(play_one[x])]))
        
    if readhand(play_one[x]) < readhand(play_two[x]):
        play_one_lose += 1
#        print('Player two wins with {}'.format(hand_order[readhand(play_two[x])]))
    
    elif readhand(play_one[x]) == readhand(play_two[x]):
        if evenhand(play_one[x], play_two[x]):
            play_one_wins += 1
#            print('Player one win')
        else:
            play_one_lose += 1
#            print('Player two win')
   
print('{} player one wins'.format(play_one_wins))
print('{} player one loss'.format(play_one_lose))

#Several cases not considered on evenhand() e.g even on 
#two pairs, two of a kind etc... 

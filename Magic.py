import random
import sys

cardNames = ["creature","instant","enchantment","sorcery","redland", "whiteLand"]
cardNumbers = [22,8,10,1,11,15]

# no need for size to be bigger than 100,000 (because it will take a long time)
times = 10000


#*********** Program start ***************

# Check for user error
if len(cardNames) != len(cardNumbers):
    print("Card types and numbers don't match up!")
    sys.exit()

#*********Create deck and list to hold averages*********
deck = []
countList = []
for i in range(len(cardNumbers)):
    countList.append(0)
    for j in range(cardNumbers[i]):
        deck.append(i)
        
#*********Draw hands*********
for i in range(times):
    random.shuffle(deck)
    hand = []
    for i in range(7):
        hand.append(deck[i])
    #print(hand)
    #Keep track of totals for each card
    for i in range(len(cardNames)):
        countList[i] += hand.count(i)
    #print("Count ", countList)

#*********calculate and print averages*********
for i in range(len(cardNames)):
    print(cardNames[i], " AVG = ", countList[i]/times) 

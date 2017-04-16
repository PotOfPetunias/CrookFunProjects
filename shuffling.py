import random

#deap??

non_land = 36
land = 24
total = non_land + land

#****************************** Utility Functions *****************
def cut(deck):
    m = random.randint(int(len(deck)/4), int(3*(len(deck)/4))) 
    return deck[:m], deck[m:]

def takeFront(deck, n):
    newDeck = deck[:n]
    leftOverDeck = deck[n:]
    return newDeck, leftOverDeck
def takeBack(deck, n):
    newDeck = deck[n:]
    leftOverDeck = deck[:n]
    return newDeck, leftOverDeck

#********************** Diffrent shuffling Functions *****************
def fancyCut(deck):
    fh, lh = cut(deck)
    ffh, flh = cut(fh)
    lfh, llh = cut(lh)
    return llh + lfh + flh + ffh
    
def shuffle(deck):
    fh, lh = cut(deck)
    newDeck = []
    while len(newDeck) < 60:
        if len(fh) >= 7:
            n = random.randint(1,7)
            s, fh = takeFront(fh, n)
            newDeck += s
        elif len(fh) != 0:
            n = random.randint(1,len(fh))
            s, fh = takeFront(fh, n)
            newDeck += s
        if len(lh) >= 7:
            n = random.randint(1,7)
            s, lh = takeFront(lh, n)
            newDeck += s
        elif len(lh) != 0:
            n = random.randint(1,len(lh))
            s, lh = takeFront(lh, n)
            newDeck += s
    return newDeck

def flipFlopDrop(deck):
    newDeck = []
    leftover = deck
    count = 0
    while len(leftover) > 0:
        if len(leftover) >= 20:
            n = random.randint(4,20)
            if count % 2 == 0:
                newDeck += leftover[:n]
                leftover = leftover[n:]
            else:
                newDeck = leftover[:n] + newDeck
                leftover = leftover[n:]
        else:
            n = random.randint(1,len(leftover))
            if count % 2 == 0:
                newDeck += leftover[:n]
                leftover = leftover[n:]
            else:
                newDeck = leftover[:n] + newDeck
                leftover = leftover[n:]
        count += 1
    return newDeck

def basicCut(deck):
    fh, lh = cut(deck)
    return lh + fh
    

#****************************** Scoring Functions ********************************
def clumpyness(deck, show = True):
    count = 0
    clumps = [0 for i in range(24)]
    for card in deck:
        if card == 1:
            count +=1
        elif count != 0:
            clumps[count - 1] += 1
            count = 0
    if count != 0:
        clumps[count - 1] += 1
    if show :
        for i in range(len(clumps)):
            if clumps[i] != 0:
                if clumps[i] == 1:
                    print(clumps[i], " clump of ", i+1)
                else:
                    print(clumps[i], " clumps of ", i+1)
    return clumps   

def expoScore(clumps):
    score = 0
    for i in range(len(clumps)):
        score += (2*clumps[i])**i+1
    return score

def score(clumps):
    score = 0
    for i in range(3,len(clumps)):
        score += (i+1)*clumps[i]
    return score
    
#****************************** Evolutionary Functions ******************************
def testShuffleMethod(iMatrix, times):
    print("do evolution")

   
#****************************** Program start *******************************

deck = [1 for i in range(24)] + [0 for i in range(36)] 
#print(deck)

times = 100
totes = [0 for i in range(24)]
avgScore = 0
for i in range(times):
    deck_s = deck
    #random.shuffle(deck)
    deck_s = flipFlopDrop(deck_s)
    #deck_s = shuffle(deck_s)
    #deck_s = fancyCut(deck_s)
    counts = clumpyness(deck_s, show = False)
    for i in range(len(counts)):
        totes[i] += counts[i]
    avgScore += score(counts)

for i in range(len(totes)):
    totes[i] = totes[i]/times
#for i in range(len(totes)): print(totes[i], "\t", i+1, " clumps")
avgScore = avgScore/times
print(avgScore)






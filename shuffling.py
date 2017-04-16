'''
Author: Lowell Crook
Date: 4/16/2017
Description:
This is a fun little project that I did to try and determine the best
way to shuffle a Magic the Gathering deck. I this game you build a deck
of cards that include mana cards and non-mana cards. When playing the game, you
want you deck to be sufficiently shuffled so that you do not have all your
mana cards clumped together.

In this project, I first made some functions that imitated shuffling methods
that real people can do with a deck of cards. Then I made a way to measure the relative
clumpyness of the shuffled deck. Then comes the fun part, I chose a random number of 
times to repeat these shuffle methods and a random order to do them. Then, I 
measure the clumpyness of the resulting deck. After that I apply a little bit of 
randomization to the order and repetition of the shuffling and test again. With this 
method I can find a good shuffling method without just testing every possible 
method. In other words I can at least find a local maximum best shuffling method.
'''
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

def alexCut(deck):
    numOfParts = random.randint(3,6)
    maxPartSize = int(len(deck)/numOfParts)
    newDeck = []
    leftover = deck
    for i in range(numOfParts-1):
        partSize = random.randint(7,maxPartSize)
        newDeck = leftover[:partSize] + newDeck
        leftover = leftover[partSize:]
    newDeck = leftover + newDeck
    return newDeck
  

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
    
#****************************** Evolutionary Utility Functions ******************************
def testShuffleMethod(deck, instMatrix, times):
    avgScore = 0
    for i in range(times):
        for instruct in instMatrix:
            if instruct == 0:
                deck = fancyCut(deck)
            elif instruct == 1:
                deck = shuffle(deck)
            elif instruct == 2:
                deck = flipFlopDrop(deck)
            elif instruct == 3:
                deck = basicCut(deck)
            elif instruct == 4:
                deck = alexCut(deck)
        clumps = clumpyness(deck, show = False)
        avgScore += score(clumps)
    return avgScore/times

def randInstruction(size):
    instMatrix = [0 for i in range(size)]
    for i in range(size):
        instMatrix[i] = random.randint(0,4)
    return instMatrix

def applyJitter(instMatrix):
    index1 = random.randint(0,len(instMatrix)-1)
    index2 = random.randint(0,len(instMatrix)-1)
    instMatrix[index1], instMatrix[index2] = instMatrix[index2], instMatrix[index1]
    i = random.randint(0,len(instMatrix)-1)
    if instMatrix[i] <= 0:
        instMatrix[i] += random.randint(0,1)
    elif instMatrix[i] >= 4:
        instMatrix[i] += random.randint(-1,0)
    else:
        instMatrix[i] += random.randint(-1,1)
    return instMatrix

#****************************** Program start *******************************

deck = [0 for i in range(15+6)] + [1 for i in range(24)] + [0 for i in range(15)] 
generations = 100
repeatTest = 100
numOfShuffles = 5

inst = randInstruction(numOfShuffles)
#inst = [1,1,1,1,1,1,1,1,1,1]
print("Starting individual ", inst)
orignalScore = testShuffleMethod(deck, inst, repeatTest)

for i in range(generations):
    instNew = applyJitter(inst)
    scoreOld = testShuffleMethod(deck, inst, repeatTest)
    scoreNew = testShuffleMethod(deck, instNew, repeatTest)
    if scoreNew < scoreOld:
        inst = instNew
        #print("Better ", inst)

print("Winning individual ", inst)
afterScore = testShuffleMethod(deck, inst, repeatTest)
print("Old: ", orignalScore, "\nNew: ", afterScore)


##scores = []
##for num in range(20):
##    inst = [1 for i in range(num)]
##    scores.append(testShuffleMethod(deck, inst, repeatTest))
##print(scores)





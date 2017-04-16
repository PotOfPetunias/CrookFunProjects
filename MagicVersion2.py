import random
import sys
import copy


class Card:
    isLand = False
    isWhite = False
    isRed = False
    name = ''
    colorless = 0
    white = 0
    red = 0
    cardType = ''
    def __init__(self,name,colorless,white,red,cardType, isLand = False):
        if isLand:
            self.isLand = isLand
            if white > 0:
                self.isWhite = True
            else:
                self.isRed = True
        else:
            self.name = name
            self.colorless = colorless
            self.white = white
            self.red = red
            self.cardType = cardType
    def __str__(self):
        if self.isLand:
            if self.isWhite:
                return 'White Land\n'
            elif self.isRed:
                return 'Red Land\n'
        output = self.name + " : " + self.cardType + '\n'
        if self.colorless != 0:
            output += self.colorless + ' colorless' + '\n'
        if self.red != 0:
            output += self.red + ' red' + '\n'
        if self.white != 0:
            output += self.white + ' white' + '\n'
        return output
    def isCreature(self):
        if self.cardType.lower() == 'creature':
            return True
        else:
            return False
    def canBePlayed(self, redMana, whiteMana):
        if int(self.colorless) > ((whiteMana - int(self.white)) + (redMana - int(self.red))):
            return False
        elif int(self.white) > whiteMana:
            return False
        elif int(self.red) > redMana:
            return False
        else:
            return True
            
                        

def playGame(deck, readGame = True, giveStats = True):
    hand = []
    table = []
    whiteMana = 0
    redMana = 0
    creaturesPlayedCount = 0
    nonCreaturesPlayedCount = 0
    emptyCount = 0
    discardCount = 0
    moreManaCount = 0
    noLandCount = 0
    noCreaturesCount = 0
    
    #*** Draw hand ***
    for i in range(7):
        hand.append(deck.pop(0))
    turns = random.randint(30,50)
    if readGame: print('First hand')
    for card in hand:
        if readGame: print(card)
    if readGame: print('******************************************************\n')

    #*** Game ***
    if readGame: print('FIRST TURN!\n')
    for turn in range(turns):
        #*** Draw card ***
        hand.append(deck.pop(0))
        if readGame: print('Draw... ', hand[len(hand)-1])

        onTable = len(table)
        #*** Play Land ***
        for i in range(len(hand)):
            if hand[i].isLand and hand[i].isWhite:
                if readGame: print('play white land\n')
                table.append(hand.pop(i))
                whiteMana += 1
                break
            elif hand[i].isLand and hand[i].isRed:
                if readGame: print('play red land\n')
                table.append(hand.pop(i))
                redMana += 1
                break
        if len(table) == onTable:
            noLandCount += 1
            if readGame: print('no land to play\n')
        
        #*** Play Spells ***
        onTable = len(table)
        haveNotPlayed = True
        couldPlay = False
        haveCreature = False
        if len(hand) > 0:
            for i in range(len(hand)):
                if i >= len(hand):
                    break
                if hand[i].isLand:
                    continue
                elif hand[i].isCreature():
                    haveCreature = True
                    if hand[i].canBePlayed(redMana, whiteMana) and haveNotPlayed:
                        if readGame: print('playing creature\n', 'redMana: ', redMana, 'whiteMana: ', whiteMana, '\n', hand[i])
                        table.append(hand.pop(i))
                        creaturesPlayedCount += 1
                        break   
                elif hand[i].canBePlayed(redMana, whiteMana) and haveNotPlayed:
                    couldPlay = True
                    if turn % 5 == 3:
                        table.append(hand.pop(i))
                        nonCreaturesPlayedCount += 1
                        haveNotPlayed = False
                        if readGame: print('playing non-creature\n', 'redMana: ', redMana, 'whiteMana: ', whiteMana, '\n', hand[i])
                        
        else:
            emptyCount += 1
            if readGame: print("hand empty\n")

        if haveCreature:
            if len(table) == onTable:
                moreManaCount += 1
                if readGame: print("We didn't have enough mana to play any creatures\n")      
        else:
            noCreaturesCount += 1
            if (len(table) == onTable):
                if couldPlay:
                    if readGame: print("We have no creatures! And we are saving non-creatures\n")
                else:
                    moreManaCount += 1
                    if readGame: print("Not enough mana to play anything from hand\n")

        #*** Discard ***
        while len(hand) > 7:
            if readGame: print('hand full discarding\n')
            discardCount += 1
            deadCard = hand.pop(0)
            if readGame: print(deadCard)
            
        if readGame: print('\nNEXT TURN hand size = ', len(hand),'\n')

    #*** Print stuff ***
    if giveStats: print('Creatures played: ', creaturesPlayedCount,
          '\nNon-Creatures played: ', nonCreaturesPlayedCount,
          '\nEmpty hands: ', emptyCount,
          '\nNo land in hand: ', noLandCount,
          '\nDiscarded: ', discardCount,
          '\nNeeded more mana: ', moreManaCount,
          '\nHad no creatures: ', noCreaturesCount,
          '\nTotal red mana: ', redMana,
          '\nTotal white mana: ', whiteMana,
          '\nTotal turns: ', turns)

    results = [creaturesPlayedCount,nonCreaturesPlayedCount,
               emptyCount,noLandCount,discardCount, moreManaCount,
               noCreaturesCount,redMana,whiteMana,turns]
            
    return results

#*********************************Program Start***********************************

f = open('RedWhiteDeck.txt')
cards = f.readlines()
f.close()
deck = []
for i in range(len(cards)):
    cards[i] = cards[i].strip()
    if cards[i][0] == '#':
        continue
    elif cards[i][0] == '@':
        landValues = cards[i].split("\t")
        white = int(landValues[1])
        red = int(landValues[2])
        for i in range(white):
            deck.append(Card('Land',0,1,0,'Land',isLand = True))
        for i in range(red):
            deck.append(Card('Land',0,0,1,'Land',isLand = True))
    else:
        cardAtt = cards[i].split("\t")
        deck.append(Card(cardAtt[0],cardAtt[1],cardAtt[2],cardAtt[3],cardAtt[4]))

times = 1
deckCopy = copy.copy(deck)
random.shuffle(deckCopy)
averages = playGame(deckCopy, readGame = True, giveStats = True)
for i in range(times - 1):
    deckCopy = copy.deepcopy(deck)
    random.shuffle(deckCopy)
    results = playGame(deckCopy, readGame = False, giveStats = False)
    for i in range(len(averages)):
        averages[i] += results[i]

for i in range(len(averages)):
    averages[i] = averages[i]/times

print('\nAverages\n')
print('Creatures played: ', averages[0],
          '\nNon-Creatures played: ', averages[1],
          '\nEmpty hands: ', averages[2],
          '\nNo land in hand: ', averages[3],
          '\nDiscarded: ', averages[4],
          '\nNeeded more mana: ', averages[5],
          '\nHad no creatures: ', averages[6],
          '\nTotal red mana: ', averages[7],
          '\nTotal white mana: ', averages[8],
          '\nTotal turns: ', averages[9])
    


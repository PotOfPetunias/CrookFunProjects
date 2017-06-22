#Crossword Maker
#Lowell Crook
#12/24/2016
import random
import traceback
##def matPrint(m):
##    output = ''
##    for row in m:
##        for i in row:
##            output += i + ' '
##        output += '\n'
##    return output

puzz = []
words = []

##class Word:
##    x = -1
##    y = -1
##    word = ''
##    def __init__(self,x,y,word):
##        self.x = x
##        self.y = y
##        self.word = word

class Direction():
    north = 1
    northE = 2
    east = 3
    southE = 4
    south = 5
    southW = 6
    west = 7
    northW = 8
    @staticmethod
    def rand():
        return random.randint(1,8)

def formatPuzzle():
    global puzz
    global words
    output = ''
    for i in words:
        output += i + '\t'
    output += '\n'
    output += '\n'.join([' '.join([i for i in row]) for row in puzz])
    return output

def add(word, m):
    word = word.upper()
    size = len(m)
    direc = Direction.rand()
    
    #**************************** Write going north **************************************
    if direc == Direction.north:
        col = random.randint(0, size - 1)
        row = random.randint(len(word) - 1, size - 1)
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            r -= 1
        for l in word:   
            m[row][col] = l
            row -= 1
        return m
    #**************************** Write going north east **************************************
    elif direc == Direction.northE:
        col = random.randint(0, size - len(word))
        row = random.randint(len(word) - 1, size - 1)
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            r -= 1
            c += 1
        for l in word:
            m[row][col] = l
            row -= 1
            col += 1
        return m
    #**************************** Write going east **************************************
    elif direc == Direction.east:
        col = random.randint(0, size - len(word))
        row = random.randint(0, size - 1)
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            c += 1
        for l in word:
            m[row][col] = l
            col += 1
        return m
    #**************************** Write going south east **************************************
    elif direc == Direction.southE:
        col = random.randint(0, size - len(word))
        row = random.randint(0, size - len(word))
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            r += 1
            c += 1
        for l in word:
            m[row][col] = l
            row += 1
            col += 1
        return m
    #**************************** Write going south **************************************
    elif direc == Direction.south:
        col = random.randint(0, size - 1)
        row = random.randint(0, size - len(word))
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            r += 1
        for l in word:
            m[row][col] = l
            row += 1
        return m
    #**************************** Write going south west **************************************
    elif direc == Direction.southW:
        col = random.randint(len(word) - 1, size - 1)
        row = random.randint(0, size - len(word))
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            r += 1
            c -= 1
        for l in word:
            m[row][col] = l
            row += 1
            col -= 1
        return m
    #**************************** Write going west **************************************
    elif direc == Direction.west:
        col = random.randint(len(word) - 1, size - 1)
        row = random.randint(0, size - 1)
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            c -= 1
        for l in word:
            m[row][col] = l
            col -= 1
        return m
    #**************************** Write going north west **************************************
    elif direc == Direction.northW: 
        col = random.randint(len(word) - 1, size - 1)
        row = random.randint(len(word) - 1, size - 1)
        c = col
        r = row
        for l in word:
            if (m[r][c] != '') and (m[r][c] != l):
                return 'fail'
            r -= 1
            c -= 1
        for l in word:
            m[row][col] = l
            row -= 1
            col -= 1
        return m
    else:
        return 'fail'

def makePuzzle(words):
    count = 0
    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    words.sort(key = len, reverse = True)
    n = len(words[0]) + 10
    puzzle = [['' for x in range(n)] for y in range(n)]

    for w in reversed(range(len(words))):
        for i in range(6):
            newPuzzle = add(words[w], puzzle)
            if type(newPuzzle) is str:
                #print(str(i+1) + 'fail')
                if i == 5:
                    print('Total falure on word: ' + words[w])
                    count += 1
                    words.remove(words[w])
            else:
                puzzle = newPuzzle
                break

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[j][i] == '':
                puzzle[j][i] = random.choice(l)

#    Use this if you want to see the words in the puzzle
##    for i in range(len(puzzle)):
##        for j in range(len(puzzle[i])):
##            if puzzle[j][i] == '':
##                puzzle[j][i] = '.'

    return (puzzle, count)

def find(word):
    global puzz
    x, y = 0, 0
    word = word.upper()
    for i in range(len(puzz)):
        for j in range(len(puzz[i])):
            if puzz[i][j] == word[0]:
                x = i
                y = j
                if checkLetter(word, x, y):
                    return word, x, y
    return word, -1, -1

def answers():
    global puzz
    global words
    coords = []
    output = ''
    for w in words:
        w, x, y = find(w)
        output += w + ' (' + str(x) + ', ' + str(y) + ')\n'
    output = output.rstrip()
    print(output)
    

def checkLetter(word, x, y):
    global puzz
    match = False
    
    for i in range(-1,2):
        for j in range(-1,2):
            try: 
                if puzz[x + i][y + j] == word[1]:
                    tempX = x + i
                    tempY = y + j
                    count = 2
                    going = True
                    while going and count < len(word):
                        tempX += i
                        tempY += j
                        if puzz[tempX][tempY] != word[count]:
                            going = False
                        elif count == len(word) - 1:
                            match = True
                        count += 1
            except IndexError:
                break
            except:
                traceback.print_exc()
                
    return match

def randWords(lib, num):
    words = []
    for i in range(num):
        words.append(random.choice(lib))
    return list(set(words))
    
#************************************* End of functions ********************************************
numOfFails = 0
numOfTry = 1
numOfWords = 20


f = open('words.txt')
lib = f.readlines()
f.close()
for i in range(len(lib)):
   lib[i] = lib[i].strip()


# Use this code if you added things to the file
#lib = list(set(lib))
##lib.sort(key = len, reverse = True)
##f = open('/Applications/Python 3.5/words.txt', 'w')
##for s in lib:
##    f.write(s)
##    f.write('\n')
##f.close()

for i in range(numOfTry):
    words = randWords(lib, numOfWords)
    puzz, n = makePuzzle(words)
    numOfFails += n
    print(formatPuzzle())






##numOfTry = numOfTry*len(words)
##print((numOfFails/numOfTry)*100, 'Percent Falure')
##print(numOfFails, '/', numOfTry)


##words = ['word','fun','crossword','computer','cube','headphones',
##            'sunglasses','drone','legos', 'remotecontrol','trust',
##            'rake', 'direction', 'vivacious', 'fall', 'town', 'oldfashioned',
##            'stuff', 'snow', 'bottle', 'yell', 'flower']








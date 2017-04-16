import time
import random


def countWords(st):
    count = 0
    wordList = st.split(" ")
    for word in wordList:
        if len(word) > 0:
            count += 1
    return count

def checkInput(orig, user):
    if(orig == user):
        print("You typed the sentence correctly!")
    else:
        orig = orig.split()
        user = user.split()
        if(len(orig) == len(user)):
            for i in range(len(orig)):
                if(orig[i] != user[i]):
                    print("You misspelled ", orig[i].strip())
        elif len(orig) > len(user):
            print("You didn't finish the sentence")
        else:
            print("You hit the space bar too many times")

def runTest():
    testSentance = random.choice(testList)
    print(testSentance)
    input("Type the sentance above:\nPress enter to start")
    start = time.clock()
    userIn = input()
    finish = time.clock()
    checkInput(testSentance, userIn)
    total = finish - start
    total = round(total/60, 3)
    numOfWords = countWords(userIn)
    wpm = round(numOfWords/total, 3)
    return total, wpm
    
#**************************** End of functions ****************************
userIn = input("Enter your name: ")
playerName = userIn

#****************************** Open files ********************************
inputFile = 'TypingTestData\\'
inputFile += playerName
inputFile += '.txt'

f = open('sentances.txt')
testList = f.readlines()
f.close()
for i in range(len(testList)):
    testList[i] = testList[i].strip()

try:
    f = open(inputFile, 'r')
    data = f.readlines()
    f.close()
    print("Save file found!")
except:
    print("Save file not found! \nCreating new save file")
    f = open(inputFile, 'w+')
    data = f.readlines()
    f.close()
    
avg = 0
totalWpm = 0
count = 0

for i in range(len(data)):
    data[i] = data[i].strip()
    if i == 0:
        avg = float(data[i])
    elif i == 1:
        count = int(data[i])
totalWpm = avg*count
print("Your current average is ", avg)
print("Your current count is ", count)

# **************************** Start game *********************************
again = True
while(again):
    again = False
    
    # Run test and get the results
    tempTotal, tempWPM = runTest()

    # Interpret and print results
    print("This test took you ",tempTotal, " minutes to complete")
    print("That's ", tempWPM, " words per minute")

    # Save this test? play again?
    userIn = input("Do you want to keep this run? ")
    userIn = userIn.lower()
    userIn = userIn.strip()
    if(userIn == "y" or userIn == "yes" or userIn == "yep" or userIn == ""):
        totalWpm += tempWPM
        count += 1
        avg = round(totalWpm/count,3)
        print("That makes your average ", avg)
    else:
        print("This run was deleted\nYour avg is still ", avg)
    userIn = input("Again? ")
    userIn = userIn.lower()
    userIn = userIn.strip()
    if(userIn == "y" or userIn == "yes" or userIn == "yep" or userIn == ""):
        again = True

# *************************** Save this game's data *************************
f = open(inputFile, 'w')
f.write(str(avg))
f.write("\n")
f.write(str(count))
f.close()





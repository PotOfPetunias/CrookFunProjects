import os
import sys

try:
    #************************* CHANGE THIS **************************
    os.chdir("C:\\Users\\lhcro\\AppData\\Local\\Cockatrice\\Cockatrice\\decks")
    #****************************************************************
    
except FileNotFoundError:
    print(os.getcwd() + "\nNot a valid directory")
    sys.exit()
    
if not os.path.exists("DeckGen"):
    os.makedirs("DeckGen")
    print('You don\'t have any files yet...\n' + 'DeckGen folder created put your files in there')
    sys.exit()
    

fileName = input("Enter the name of the file: ")

inFilePath = "DeckGen\\" + fileName + ".txt"


# ******************** Program Start ********************
cardString = "        <card number=\"\" price=\"0\" name=\"\"/>\n"

def getHeader():
    output = ""
    output += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    output += "<cockatrice_deck version=\"1\">\n"
    output += "    <deckname></deckname>\n"
    output += "    <comments></comments>\n"
    output += "    <zone name=\"main\">\n"
    return output
def getTail():
    output = ""
    output += "    </zone>\n"
    output += "</cockatrice_deck>"
    return output
def insertData(count, name):
    return cardString[:22] + str(count) + cardString[22:40] + name + cardString[40:]


#******* Read input *******
try:
    file = open(inFilePath)
    lines = file.readlines()
    file.close()
except IOError:
    print("File not found")
    sys.exit()
    

#******* Translate input *******
counts = []
names = []
for i in range(len(lines)):
    l = lines[i]
    try:
        l.index("x")
    except:
        continue
    count = 0
    try:
        count = int(l[:l.index("x")])
    except ValueError:
        continue
    counts.append(count)
    if l[-1] == "\n":
        names.append(l[l.index("x")+2:-1])
    else:
        names.append(l[l.index("x")+2:])


#******* Write output *******
fileName + ".cod"
file = open(fileName + ".cod", 'w')
file.write(getHeader())

for i in range(len(names)):
    print("Adding ", counts[i], " ", names[i], "cards")
    file.write(insertData(counts[i], names[i]))
    
file.write(getTail())
file.close()

print("Deck ready")


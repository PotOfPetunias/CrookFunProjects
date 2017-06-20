import time
#from datetime import date
from datetime import datetime

isTest = False
visitorNumber = 0

#***********Better way probably********
def contains(code, thing):
    i = code.find(thing)
    if i < 0:
        return False
    return True
#^^^^^^^^^^^^^^^Better way probably^^^^^^^^^

def howMany(code, index):
    if index < 0:
        return 0
    if index == 0:
        return 1
    try:
        return int(code[index - 1])
    except ValueError:
        return 1
    

def guestDeCode(code):
    #*********Data*********
    vehicle = 'Passenger Vehicle'
    adults = 0
    seniors = 0
    kids = 0
    dogs = 0
    overnight = False
    camping = False
    cabin = False
    parkPass = 'No Pass'
    
    #*********How Many People*********
    aIndex = code.find("a")
    sIndex = code.find("s")
    kIndex = code.find("k")
    dIndex = code.find("d")
    adults = howMany(code, aIndex)
    seniors = howMany(code, sIndex)
    kids = howMany(code, kIndex)
    dogs = howMany(code, dIndex)
    
    #*********Overnight?*********
    camping = contains(code, 'cg')
    cabin = contains(code, 'c') and not camping 
    if camping or cabin:
        overnight = True
    
    #*********Do they have a pass*********
    if contains(code, 'fp'):
        parkPass = 'Family Pass'
    if contains(code, 'sp'):
        parkPass = 'Senior Pass'
    if contains(code, 'ip'):
        parkPass = 'Individual Pass'

    #*********What Vehicle?*********
    if contains(code, 'rv'):
        vehicle = 'RV'
    elif contains(code, 'b'):
        vehicle = 'Bike'
    elif contains(code, 'm'):
        vehicle = 'Motercycle'
    elif contains(code, 'w'):
        vehicle = 'Walking'
    
    #*********Record Data*********
    if contains(code, 'v') and vehicle != 'RV':
        record(vehicle, adults, seniors, kids, dogs, overnight, camping, cabin, parkPass, vbas = True)
    else:
        record(vehicle, adults, seniors, kids, dogs, overnight, camping, cabin, parkPass)

    

def record(vehicle, adults, seniors, kids, dogs, overnight, camping, cabin, parkPass,
           turn = False, reEntry = False, vbas = False):
    
    global visitorNumber
    
    t = datetime.now()
    date = str(t.month) +"/"+ str(t.day) +"/"+ str(t.year)
    time = str(t.hour) +":"+ str(t.minute) +":"+ str(t.second)
    print(date, ' ', time)
    
    if turn:
        print('Turn Around')
    elif reEntry:
        print('Visitor Re-Entry')
    else:
        if vbas:
            print('Going to VBAS')
        print(vehicle, ', ', adults, ' Adults, ',
              seniors, ' Seniors, ',
              kids, ' kids, ',
              dogs, ' dogs \n',
              'overnight:', overnight,
              ', camping:', camping,
              ', cabin:', cabin,
              ', parkPass:', parkPass)
        
    if isTest:
        print('\nProgram is in test mode and will not record any data!\n',
              'to exit test mode and start recording type \"end\"')
    else:
        visitorNumber += 1
        file = open('MNSOData.csv',"a")
        file.write(str(visitorNumber))
        file.write(',')
        file.write(date)
        file.write(',')
        file.write(time)
        file.write(',')
        file.write(vehicle)
        file.write(',')
        file.write(str(adults))
        file.write(',')
        file.write(str(seniors))
        file.write(',')
        file.write(str(kids))
        file.write(',')
        file.write(str(dogs))
        file.write(',')
        file.write(str(overnight))
        file.write(',')
        file.write(str(camping))
        file.write(',')
        file.write(str(cabin))
        file.write(',')
        file.write(parkPass)
        if turn:
            file.write(',')
            file.write('Turn Around')
        elif reEntry:
            file.write(',')
            file.write('Visitor Re-Entry')
        elif vbas:
            file.write(',')
            file.write('Going to VBAS')
        file.write('\n')
        file.close()

def turnAround():
    record('na', 0, 0, 0, 0, 'na', 'na', 'na', 'na', turn = True)
def reEntry():
    record('na', 0, 0, 0, 0, 'na', 'na', 'na', 'na', reEntry = True)

def remove():
    return 0

def getLastEntry():
    file = open('MNSOData.csv',"r")
    lines = file.readlines()   #***********Better way probably*************************************************
    lastLine = lines[-1]
    entryNum = lastLine[:lastLine.index(',')]
    return int(entryNum)

def helpMenu():
    print('****************************Help***********************************\n',
          'Designed by Lowell Crook\n',
          '\tThis program was made to record data about the people the enter into \n',
          'Monte Sano State Park. It was designed by a person who ran the gate for people\n',
          'who run the gate. The main priority in its design was to be fast. There is a\n',
          'system of symbols in place the represent diffrent useful information points.\n',
          'These symbols can be typed in any order and the system ignores case\n\n',
          '\tExample:  2arv  \n\n',
          'The example command represents an RV the came into the park with two adults in it\n\n\n',
          'The following is a list of the proper commands and symbols the can be used\n',
          '*********** Commands ************\n',
          'close - this command closes the program \n',
          'test - this command starts up test mode. This mode is for learning how to use to system\n',
          '\twithout recording any bad data\n',
          'end - this command exits the testing mode\n',
          'help - displays this help menu\n',
          'remove - NOT OPERATIONAL\n',
          '**** Quick Entry Commands **** (used for entering commen cases)\n',
          't - (stands for Turn Around) record a potential visitor turning around\n',
          'r - (stands for ReEntry) record a camper or cabin visitor comming back into the park\n\n',
          '*********** Symbols *************\n',
          'The first four symbols (a,s,k,and d) can be augmented by placing a \n',
          '\tone digit number in front of them this tells the system \"how many\" \n',
          'a - (stands for Adult)\n',
          's - (stands for Senior)\n',
          'k - (stands for Kid)\n',
          'd - (stands for Dog)\n\n',
          'b - (stands for Bike)\n',
          'm - (stands for Motercycle)\n',
          'w - (stands for Walking)\n',
          'rv - (stands for RV)\n\n',
          'cg - (stands for camp ground)\n',
          'c - (stands for cabin)\n',
          'v - (stands for going to VBAS)\n\n',
          'fp - (stands for Family Pass)\n',
          'sp - (stands for Senior Pass)\n',
          'ip - (stands for Individual Pass)\n')
          
          
#************************* Program Start *************************

visitorNumber = getLastEntry()
print('If you need help type \"help\"')
while True:
    guestCode = input("Entry: ")
    guestCode = guestCode.lower()
    guestCode = guestCode.strip()
    if guestCode == "close":
        break
    if guestCode == "t":
        turnAround()
    elif guestCode == "r":
        reEntry()
    elif guestCode == "remove":
        remove()
    elif guestCode == "test":
        isTest = True
    elif guestCode == "end":
        isTest = False
    elif guestCode == "help":
        helpMenu()
    else:
        guestDeCode(guestCode)

#open("Filename.csv", "a")

import time
#from datetime import date
from datetime import datetime

isTest = False
visitorNumber = 0

def contains(code, thing):
    i = code.find(thing)
    if i < 0:
        return False
    return True

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
    destination = 'na'
    
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
    elif contains(code, 't'):
        vehicle = 'Trailer Vehicle'
    elif contains(code, 'b'):
        vehicle = 'Bike'
    elif contains(code, 'm'):
        vehicle = 'Motercycle'
    elif contains(code, 'w'):
        vehicle = 'Walking'

    #*********What Destonation?*********
    if contains(code, 'v') and vehicle != 'RV':
        destination = 'VBAS'
    if contains(code, 'r') and vehicle != 'RV':
        destination = 'Restroom'
    if contains(code, 'l'):
        destination = 'Lodge event'
    if contains(code, 'e'):
        destination = 'Event at a pavilion'
    if contains(code, 'o'):
        destination = 'Just to the store'
    #*********Record Data*********
    if contains(code, 'n'):
        record(vehicle, adults, seniors, kids, dogs, overnight, camping, cabin, parkPass, destination, noCash = True)
    else:
        record(vehicle, adults, seniors, kids, dogs, overnight, camping, cabin, parkPass, destination)

    

def record(vehicle, adults, seniors, kids, dogs, overnight, camping, cabin, parkPass, destination,
           turn = False, reEntry = False, employee = False, noCash = False):
    
    global visitorNumber
    
    t = datetime.now()
    date = str(t.month) +"/"+ str(t.day) +"/"+ str(t.year)
    time = str(t.hour) +":"+ str(t.minute) +":"+ str(t.second)
    print(time, ' ', date)
    
    if turn:
        print('Turn Around')
    elif reEntry:
        print('Visitor Re-Entry')
    elif employee:
        print('Park Employee')
    else:
        if noCash:
            print("No Cash!")
        print(vehicle, ', ', adults, ' Adults, ',
            seniors, ' Seniors, ',
            kids, ' kids, ',
            dogs, ' dogs \n',
            'overnight:', overnight,
            ', camping:', camping,
            ', cabin:', cabin,
            ', parkPass:', parkPass,
            ', destination:', destination)
        
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
        file.write(',')
        file.write(destination)
        if turn:
            file.write(',')
            file.write('Turn Around')
        elif reEntry:
            file.write(',')
            file.write('Visitor Re-Entry')
        elif employee:
            file.write(',')
            file.write('Park Employee')
        elif noCash:
            file.write(',')
            file.write('No Cash')
        file.write('\n')
        file.close()

##def undo():
##    lineNum = getLastEntry()
##    file = open('MNSOData.csv',"r+")
##    line = file.readline()
##    #for i in range(lineNum -1):
##        #line = file.readline()
##    file.write(str(lineNum))
##    file.write(',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,This line was erased!!!!!!!!!!\n')
##    file.close()
##
def getLastEntry():
    file = open('MNSOData.csv',"r")
    buff = ''
    line = file.readline() 
    while True:
        if line == '':
            break
        buff = line
        line = file.readline()
    entryNum = buff[:buff.index(',')]
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
          'test  - this command starts up test mode. This mode is for learning how to use to system\n',
          '\t without recording any bad data\n',
          'end   - this command exits the testing mode\n',
          'help  - displays this help menu\n',
          'undo  - NOT OPERATIONAL\n\n',
          '**** Quick Entry Commands **** (used for entering commen cases)\n',
          't - (stands for Turn Around) record a potential visitor turning around\n',
          'p - (stands for Park Employee) record an Employee coming into the park\n',
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
          't - (stands for Trailer vehicle)\n',
          'rv - (stands for RV)\n\n',
          'cg - (stands for camp ground)\n',
          'c - (stands for cabin)\n',
          'l - (stands for lodge event)\n',
          'e - (stands for Event in another place besides the lodge)\n',
          'v - (stands for VBAS)\n',
          'o - (stands for Office or Store) going just to the store and back\n',
          'r - (stands for Restroom)\n\n',
          'fp - (stands for Family Pass)\n',
          'sp - (stands for Senior Pass)\n',
          'ip - (stands for Individual Pass)\n\n',
          'n - (stands for No cash)\n\n')
          
          
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
        record('na', 0, 0, 0, 0, 'na', 'na', 'na', 'na', 'na', turn = True)
    elif guestCode == "r":
        record('na', 0, 0, 0, 0, 'na', 'na', 'na', 'na', 'na', reEntry = True)
    elif guestCode == "p":
        record('na', 0, 0, 0, 0, 'na', 'na', 'na', 'na', 'na', employee = True)
    elif guestCode == "remove":
        remove()
    elif guestCode == "test":
        isTest = True
        print('Entering test mode')
    elif guestCode == "end":
        isTest = False
        print('Leaving test mode')
    elif guestCode == "help":
        helpMenu()
    elif guestCode == '':
        print('No action')
    else:
        guestDeCode(guestCode)

#open("Filename.csv", "a")
##def getLastEntry():
##    file = open('MNSOData.csv',"r")
##    lines = file.readlines()   #***********Better way probably*************************************************
##    lastLine = lines[-1]
##    entryNum = lastLine[:lastLine.index(',')]
##    return int(entryNum)
        import time
##import os
##from collections import deque
##from datetime import datetime
##
##visitorNumber = 0
##
##class Entry:
##    date = 0
##    time = 0
##    vehicle = 'na'
##    adults = 0
##    seniors = 0
##    kids = 0
##    dogs = 0
##    overnight = False
##    camping = False
##    cabin = False
##    parkPass = 'na'
##    destination = 'na'
##    notes = ''
##    
##    def __init__(self,code):
##        t = datetime.now()
##        self.date = str(t.month) +"/"+ str(t.day) +"/"+ str(t.year)
##        self.time = str(t.hour) +":"+ str(t.minute) +":"+ str(t.second)
##        if self.decodeSpecial(code):
##            self.decodeGuest(code)
##            self.decodeVehicle(code)
##            self.decodeDestination(code)
##            self.decodePass(code)
##            self.decodeOverNight(code)
##        
##    def decodeGuest(self, code):
##        aIndex = code.find("a")
##        sIndex = code.find("s")
##        kIndex = code.find("k")
##        dIndex = code.find("d")
##        self.adults = howMany(code, aIndex)
##        self.seniors = howMany(code, sIndex)
##        self.kids = howMany(code, kIndex)
##        self.dogs = howMany(code, dIndex)
##        
##    def decodeVehicle(self, code):
##        if contains(code, 'rv'):
##            self.vehicle = 'RV'
##        elif contains(code, 't'):
##            self.vehicle = 'Trailer Vehicle'
##        elif contains(code, 'b'):
##            self.vehicle = 'Bike'
##        elif contains(code, 'm'):
##            self.vehicle = 'Motercycle'
##        elif contains(code, 'w'):
##            self.vehicle = 'Walking'
##        else:
##            self.vehicle = 'Passenger Vehicle'
##
##    def decodeDestination(self, code):
##        if contains(code, 'v') and self.vehicle != 'RV':
##            self.destination = 'VBAS'
##        elif contains(code, 'r') and self.vehicle != 'RV':
##            self.destination = 'Restroom'
##        elif contains(code, 'l'):
##            self.destination = 'Lodge event'
##        elif contains(code, 'e'):
##            self.destination = 'Event at a pavilion'
##        elif contains(code, 'o'):
##            self.destination = 'Just to the store'
##        elif contains(code, 'g'):
##            self.destination = 'Campground'
##        elif contains(code, 'c'):
##            self.destination = 'Cabins'
##        else:
##            self.destination = 'na'
##    
##    def decodePass(self, code):
##        if contains(code, 'fp'):
##            self.parkPass = 'Family Pass'
##        elif contains(code, 'sp'):
##            self.parkPass = 'Senior Pass'
##        elif contains(code, 'ip'):
##            self.parkPass = 'Individual Pass'
##        else:
##            self.parkPass = 'No Pass'
##
##    def decodeOverNight(self, code):
##        self.camping = contains(code, 'g')
##        self.cabin = contains(code, 'c')
##        self.overnight = self.camping or self.cabin
##
##    def decodeSpecial(self, code):
##        if code == "t":
##            self.notes = 'Turn Around'
##            return False
##        elif code == "r":
##            self.notes = 'Visitor Re-Entry'
##            return False
##        elif code == "p":
##            self.notes = 'Park Employee'
##            return False
##        elif contains(code, 'n'):
##            self.notes = 'No Cash'
##            return True
##        return True
##    
##    def display(self):
##        print(self.time, ' ', self.date)
##        print(self.vehicle, ', ', self.adults, ' Adults, ',
##            self.seniors, ' Seniors, ',
##            self.kids, ' kids, ',
##            self.dogs, ' dogs',
##            '\novernight:', self.overnight,
##            ', camping:', self.camping,
##            ', cabin:', self.cabin,
##            ', parkPass:', self.parkPass,
##            ', \ndestination:', self.destination,
##            ', notes:', self.notes)
##
##def contains(code, thing):
##    i = code.find(thing)
##    if i < 0:
##        return False
##    return True
##
##def howMany(code, index):
##    if index < 0:
##        return 0
##    if index == 0:
##        return 1
##    try:
##        return int(code[index - 1])
##    except ValueError:
##        return 1
##
##def getLastEntry():
##    file = open('Test.csv',"r")
##    buff = ''
##    line = file.readline() 
##    while True:
##        if line == '':
##            break
##        buff = line
##        line = file.readline()
##    entryNum = buff[:buff.index(',')]
##    return int(entryNum)
##
##def record(entry):
##    global visitorNumber
##    visitorNumber += 1
##    file = open('Test.csv',"a")
##    line = [str(visitorNumber), ',', entry.date, ',',entry.time,',',
##            entry.vehicle, ',',str(entry.adults), ',',str(entry.seniors),',',
##            str(entry.kids), ',',str(entry.dogs), ',',str(entry.overnight),',',
##            str(entry.camping), ',',str(entry.cabin), ',',entry.parkPass,',',
##            entry.destination, ',',entry.notes, '\n']
##    
##    file.writelines(line)
##    file.close()
##
##
##def helpMenu():
##    print('****************************Help***********************************\n',
##          'Designed by Lowell Crook\n',
##          '\tThis program was made to record data about the people the enter into \n',
##          'Monte Sano State Park. It was designed by a person who ran the gate for people\n',
##          'who run the gate. The main priority in its design was to be fast. There is a\n',
##          'system of symbols in place the represent diffrent useful information points.\n',
##          'These symbols can be typed in any order and the system ignores case\n\n',
##          '\tExample:  2arv  \n\n',
##          'The example command represents an RV the came into the park with two adults in it\n\n\n',
##          'The following is a list of the proper commands and symbols the can be used\n',
##          '*********** Commands ************\n',
##          'close - this command closes the program \n',
##          'test  - this command starts up test mode. This mode is for learning how to use to system\n',
##          '\t without recording any bad data\n',
##          'end   - this command exits the testing mode\n',
##          'help  - displays this help menu\n',
##          'undo  - NOT OPERATIONAL\n\n',
##          '**** Quick Entry Commands **** (used for entering commen cases)\n',
##          't - (stands for Turn Around) record a potential visitor turning around\n',
##          'p - (stands for Park Employee) record an Employee coming into the park\n',
##          'r - (stands for ReEntry) record a camper or cabin visitor comming back into the park\n\n',
##          '*********** Symbols *************\n',
##          'The first four symbols (a,s,k,and d) can be augmented by placing a \n',
##          '\tone digit number in front of them this tells the system \"how many\" \n',
##          'a - (stands for Adult)\n',
##          's - (stands for Senior)\n',
##          'k - (stands for Kid)\n',
##          'd - (stands for Dog)\n\n',
##          'b - (stands for Bike)\n',
##          'm - (stands for Motercycle)\n',
##          'w - (stands for Walking)\n',
##          't - (stands for Trailer vehicle)\n',
##          'rv - (stands for RV)\n\n',
##          'g - (stands for camp Ground)\n',
##          'c - (stands for cabin)\n',
##          'l - (stands for lodge event)\n',
##          'e - (stands for Event in another place besides the lodge)\n',
##          'v - (stands for VBAS)\n',
##          'o - (stands for Office or Store) going just to the store and back\n',
##          'r - (stands for Restroom)\n\n',
##          'fp - (stands for Family Pass)\n',
##          'sp - (stands for Senior Pass)\n',
##          'ip - (stands for Individual Pass)\n\n',
##          'n - (stands for No cash)\n\n')
##          
##          
###************************* Program Start *************************
##testMode = False
##visitorNumber = getLastEntry()
##print('If you need help type \"help\"')
##buff = deque([])
##while True:
##    guestCode = input("Entry: ")
##    guestCode = guestCode.lower()
##    guestCode = guestCode.strip()
##    if guestCode == "close":
##        break
##    elif guestCode == '':
##        print('No action')
##    elif guestCode == "help":
##        helpMenu()
##    elif guestCode == "test":
##        testMode = True
##        print('Entering test mode')
##    elif guestCode == "end":
##        testMode = False
##        print('Leaving test mode')
##    
##    elif guestCode == "undo":
##        d = buff.pop()
##        print('Will not record entry: \n')
##        d.display()
##    
##    else:
##        x = Entry(guestCode)
##        x.display()
##        if testMode:
##            print('\nProgram is in test mode and will not record any data!\n',
##              'to exit test mode and start recording type \"end\"')
##        else:
##            buff.append(x)
##            if len(buff) > 5:
##                print('recorded entry')
##                record(buff.popleft())
##
##print('recording last entries')
##while len(buff) > 0:
##    record(buff.popleft())
##
###open("Filename.csv", "a")
####def getLastEntry():
####    file = open('MNSOData.csv',"r")
####    lines = file.readlines()
####    lastLine = lines[-1]
####    entryNum = lastLine[:lastLine.index(',')]
####    return int(entryNum)


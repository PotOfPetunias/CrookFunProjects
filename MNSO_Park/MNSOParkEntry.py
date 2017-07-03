import time
import calendar
import os
from collections import deque
from datetime import datetime
from shutil import copyfile
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\lhcro\\Documents\\(8)Summer2017\\MNSOdata')
fileName = 'MNSOData.csv'
visitorNumber = 0

def helpMenu():
    print('****************************Help***********************************\n',
          'Designed by Lowell Crook\n',
          '\tThis program was made to record data about the people the enter into \n',
          'Monte Sano State Park. It was designed by a person who ran the gate for people\n',
          'who run the gate. The main priority in its design was to be fast. There is a\n',
          'system of symbols in place the represent diffrent useful information points.\n',
          'These symbols can be typed in any order and the system ignores case\n\n',
          '\tExample:  2arv  \n\n',
          'The example command represents an RV that came into the park with two adults in it\n\n\n',
          'The following is a list of the proper commands and symbols the can be used\n',
          '*********** Commands ************\n',
          'close - this command closes the program \n',
          'test  - this command starts up test mode. This mode is for learning how to use to system\n',
          '\t without recording any bad data\n',
          'end   - this command exits the testing mode\n',
          'help  - displays this help menu\n',
          'undo  - erases the last entry (max of 5 of erases) \n\n',
          '**** Quick Entry Commands **** (used for entering commen cases)\n',
          't - (stands for Turn Around) record a potential visitor turning around\n',
          'p - (stands for Park Employee) record an Employee coming into the park\n',
          'r - (stands for ReEntry) record a camper or cabin visitor comming back into the park\n',
          'd - (stands for Deleivery) record a deleivery\n',
          'dl or ld - (stands for Deleivery to Lodge)\n\n',
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
          'rv- (stands for RV)\n\n',
          'g - (stands for camp Ground)\n',
          'c - (stands for cabin)\n',
          'u - (stands for undecided) means that they are potential paying customers \n\tand are just looking right now\n',
          'v - (stands for visiting)visiting people in campground or cabins\n',
          'l - (stands for lodge event)\n',
          'e - (stands for Event) Going to a pavillion event\n',
          'v - (stands for VBAS) because v was used for visiting a person cannot come \n\tto visit and go to vbas\n',
          'h - (stands for Huntsville High) HHS cross country team\n',
          'o - (stands for Office or Store) going just to the store and back\n',
          'j - (stands for Japanese) means they are volenteering at tea garden\n',
          'r - (stands for Restroom)\n\n',
          'fp- (stands for Family Pass)\n',
          'sp- (stands for Senior Pass)\n',
          'ip- (stands for Individual Pass)\n\n',
          'n - (stands for No cash)\n\n',
          '; - if you want to add a note for a special case then use this symbol and\n',
          '\t everything after it will go into the notes section\n')
          
class Entry:
    date = 0
    time = 0
    vehicle = 'na'
    adults = 0
    seniors = 0
    kids = 0
    dogs = 0
    overnight = False
    camping = False
    cabin = False
    parkPass = 'na'
    destination = 'na'
    notes = ''

    def create(self,line):
        data = line.split(',')
        self.date = data[1]
        self.time = data[2]
        self.vehicle = data[3]
        self.adults = int(data[4])
        self.seniors = int(data[5])
        self.kids = int(data[6])
        self.dogs = int(data[7])
        self.overnight = data[8].lower() == 'true'
        self.camping = data[9].lower() == 'true'
        self.cabin = data[10].lower() == 'true'
        self.parkPass = data[11]
        self.destination = data[12]
        self.notes = data[13].strip()
    
    def interp(self,code):
        t = datetime.now()
        self.date = str(t.month) +"/"+ str(t.day) +"/"+ str(t.year)
        self.time = str(t.hour) +":"+ str(t.minute) +":"+ str(t.second)
        nStart = code.find(';')
        if nStart != -1:
            self.notes = code[nStart + 1:]
            code = code[:nStart]
        if self.decodeSpecial(code):
            self.decodeGuest(code)
            self.decodeVehicle(code)
            self.decodeDestination(code)
            self.decodePass(code)
            self.decodeOverNight(code)
        
    def decodeGuest(self, code):
        aIndex = code.find("a")
        sIndex = code.find("s")
        kIndex = code.find("k")
        dIndex = code.find("d")
        self.adults = howMany(code, aIndex)
        self.seniors = howMany(code, sIndex)
        self.kids = howMany(code, kIndex)
        self.dogs = howMany(code, dIndex)
        
    def decodeVehicle(self, code):
        if contains(code, 'rv'):
            self.vehicle = 'RV'
        elif contains(code, 't'):
            self.vehicle = 'Trailer Vehicle'
        elif contains(code, 'b'):
            self.vehicle = 'Bike'
        elif contains(code, 'm'):
            self.vehicle = 'Motercycle'
        elif contains(code, 'w'):
            self.vehicle = 'Walking'
        else:
            self.vehicle = 'Passenger Vehicle'

    def decodeDestination(self, code):
        if contains(code, 'l'):
            self.destination = 'Lodge event'
            if contains(code, 'u'):
                self.notes = 'Looking at the Lodge'
                
        elif contains(code, 'e'):
            self.destination = 'Event at a pavilion'
            if contains(code, 'u'):
                self.notes = 'Looking at the pavilion'
                
        elif contains(code, 'g'):
            self.destination = 'Campground'
            if contains(code, 'u'):
                self.notes = 'Looking at the campground'
            elif contains(code, 'v'):
                self.notes = 'Visiting guests in the campground'
                
        elif contains(code, 'c'):
            self.destination = 'Cabins'
            if contains(code, 'u'):
                self.notes = 'Looking at the Cabins'
            elif contains(code, 'v'):
                self.notes = 'Visiting guests at the cabins'
                
        elif contains(code, 'u'):
            self.notes = 'just want to drive through really quick'
        elif contains(code, 'o'):
            self.destination = 'Just to the store'
        elif contains(code, 'j'):
            self.destination = 'Japanese garden to volenteer'
        elif contains(code, 'h'):
            self.notes = 'HHS cross country team'
        elif contains(code, 'v') and self.vehicle != 'RV':
            self.destination = 'VBAS'
        elif contains(code, 'r') and self.vehicle != 'RV':
            self.destination = 'Restroom'
        else:
            self.destination = 'na'
    
    def decodePass(self, code):
        if contains(code, 'fp'):
            self.parkPass = 'Family Pass'
        elif contains(code, 'sp'):
            self.parkPass = 'Senior Pass'
        elif contains(code, 'ip'):
            self.parkPass = 'Individual Pass'
        else:
            self.parkPass = 'No Pass'

    def decodeOverNight(self, code):
        if not (contains(code, 'u') or contains(code, 'v')):
            self.camping = contains(code, 'g')
            self.cabin = contains(code, 'c')
            self.overnight = self.camping or self.cabin

    def decodeSpecial(self, code):
        if code == "t":
            self.notes = 'Turn Around'
            return False
        elif code == "r":
            self.notes = 'Visitor Re-Entry'
            return False
        elif code == "p":
            self.notes = 'Park Employee'
            return False
        elif code == "d":
            self.notes = 'Deleivery'
            return False
        elif code == "dl" or code == "ld":
            self.notes = 'Deleivery'
            self.destination = 'Lodge event'
            return False
        elif contains(code, 'n'):
            self.notes = 'No Cash'
        return True
    
    def display(self):
        print(self.time, ' ', self.date)
        if self.vehicle != 'na':
            print(self.vehicle)
        if self.adults != 0:
            print(self.adults, ' Adults')
        if self.seniors != 0:
            print(self.seniors, ' Seniors')
        if self.kids != 0:
            print(self.kids, ' kids')
        if self.dogs != 0:
            print(self.dogs, ' dogs')
        if self.camping:
            print('Overnight guest in campground')
        if self.cabin:
            print('Overnight guest in cabin')
        if self.parkPass != 'na' and self.parkPass != 'No Pass':
            print('With ', self.parkPass)
        if self.destination != 'na':
            print('destination: ', self.destination)
        if self.notes != '':
            print('notes:', self.notes)
## End Class ##

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

def record(entry):
    global visitorNumber
    global fileName
    visitorNumber += 1
    file = open(fileName,"a")
    line = [str(visitorNumber), ',', entry.date, ',',entry.time,',',
            entry.vehicle, ',',str(entry.adults), ',',str(entry.seniors),',',
            str(entry.kids), ',',str(entry.dogs), ',',str(entry.overnight),',',
            str(entry.camping), ',',str(entry.cabin), ',',entry.parkPass,',',
            entry.destination, ',',entry.notes, '\n']
    
    file.writelines(line)
    file.close()

def getLastEntryNum():
    global fileName 
    file = open(fileName,"r")
    buff = ''
    line = file.readline() 
    while True:
        if line == '':
            break
        buff = line
        line = file.readline()
    entryNum = buff[:buff.index(',')]
    file.close()
    return int(entryNum)

def manageBackups():
    files = os.listdir()
    backups = []
    doneDailyBackup = False
    
    t = datetime.now()
    date = str(t.month) +"-"+ str(t.day) +"-"+ str(t.year)
    bName = 'SPbackup' + date + '.csv'
    
    for f in files:
        if contains(f, 'SPbackup'):
            backups.append(f)
        if f == bName:
            doneDailyBackup = True
            
    if not doneDailyBackup:
        print('Doing daily backup')
        if len(backups) < 5:
            copyfile(fileName, bName)
        else:
            ##print('Backup not done becuase there are already 5!!!!!')
            minTime = os.path.getmtime(backups[0])
            index = -1
            for i in range(len(backups)):
                checkTime = os.path.getmtime(backups[i])
                if checkTime <= minTime:
                    index = i
                    minTime = checkTime
            if index >= 0:
                copyfile(fileName, backups[index])
                os.rename(backups[index], bName)
            else:
                print('ERROR! Somehow there was no minimum time for backups')
    else:
        print('Daily backup already completed')

def getDateFromLine(line):
    try:
        return line.split(',')[1]
    except IndexError:
        return ''

def getTimeFromLine(line):
    try:
        return line.split(',')[2]
    except IndexError:
        return ''

def today():
    t = datetime.now()
    review(str(t.month), str(t.day), str(t.year))

def review(month, day, year, show = True):
    global fileName
    date = str(month) +"/"+ str(day) +"/"+ str(year)
    entries = []
    file = open(fileName,"r")
    buff = ''
    line = file.readline() 
    while True:
        if getDateFromLine(line) == date or line == '':
            break
        buff = line
        line = file.readline()
    while getDateFromLine(line) == date:
        entries.append(line)
        line = file.readline()
    file.close()

    for i in range(len(entries)):
        x = Entry()
        x.create(entries[i])
        entries[i] = x
    if show: 
        print('======== Summary of ', date, ' ========')
        showTallies(entries)
    else:
        return entries

def graphToday():
    t = datetime.now()
    graph(str(t.month), str(t.day), str(t.year))

def graph(month, day, year):
    entries = review(month, day, year, show = False)
    blocks = createTimeBlocks(entries)
    aSums = []
    sSums = []
    kSums = []
    dSums = []
    lineupk = []
    lineupd = []
    for b in blocks:
        aSums.append(0)
        sSums.append(0)
        kSums.append(0)
        dSums.append(0)
        lineupk.append(0)
        lineupd.append(0)

    xAxLabels = []
    begin = int(entries[0].time.split(':')[0])
    end = int(entries[-1].time.split(':')[0])
    xAxLabels = list(range(begin, end+1))
    for i in range(len(blocks)):
        for e in blocks[i]:
            aSums[i] += e.adults
            sSums[i] += e.seniors
            kSums[i] += e.kids
            dSums[i] += e.dogs
            lineupk[i] += (e.adults + e.seniors)
            lineupd[i] += (e.adults + e.seniors + e.kids)
    
    ind = np.arange(len(blocks))
        
    p1 = plt.bar(ind, aSums)
    p2 = plt.bar(ind, sSums, bottom=aSums)
    p3 = plt.bar(ind, kSums, bottom=lineupk)
    p4 = plt.bar(ind, dSums, bottom=lineupd)

    title = 'Visitors on ' + str(month) + '/' + str(day) + '/' + str(year)
    plt.title(title)
    plt.ylabel('Number of Guests')
    plt.xlabel('Time (in 24 hour format)')
    plt.xticks(ind, xAxLabels)
    plt.legend((p4[0], p3[0], p2[0], p1[0]), ('dogs', 'kids', 'seniors', 'adults'))
    
    plt.show()
    
def createTimeBlocks(entries):
    begin = entries[0].time
    end = entries[-1].time
    begin = begin.split(':')
    end = end.split(':')
    for i in range(len(begin)):
        begin[i] = int(begin[i])
        end[i] = int(end[i])
    index = list(range(begin[0], end[0]+1))
    blocks = []
    for i in index:
        blocks.append([])    
    for i in range(len(entries)):
        blocks[int(entries[i].time.split(':')[0]) - begin[0]].append(entries[i])
    return blocks
    
def showTallies(entryObjList):  
    aSum = 0
    sSum = 0
    kSum = 0
    dSum = 0
    
    turnArounds = 0
    carPasses = 0
    parkEmployees = 0
    deleiveries = 0

    fPasses = 0
    sPasses = 0
    iPasses = 0    
    
    aEventGuests = 0
    sEventGuests = 0
    kEventGuests = 0
    dEventGuests = 0
    
    aLodgeGuests = 0
    sLodgeGuests = 0
    kLodgeGuests = 0
    dLodgeGuests = 0
    
    overnights = 0
    aCabins = 0
    sCabins = 0
    kCabins = 0
    dCabins = 0
    aCampers = 0
    sCampers = 0
    kCampers = 0
    dCampers = 0
    
    for x in entryObjList:
        aSum += x.adults
        sSum += x.seniors
        kSum += x.kids
        dSum += x.dogs

        if x.parkPass == 'Family Pass': fPasses += 1
        elif x.parkPass == 'Senior Pass': sPasses += 1
        elif x.parkPass == 'Individual Pass': iPasses += 1
        
        if x.notes == 'Turn Around': turnArounds += 1
        elif x.notes == 'Visitor Re-Entry': carPasses += 1
        elif x.notes == 'Park Employee': parkEmployees += 1
        elif x.notes == 'Deleivery': deleiveries += 1

        if x.destination == 'Event at a pavilion':
            aEventGuests += x.adults
            sEventGuests += x.seniors
            kEventGuests += x.kids
            dEventGuests += x.dogs
        if x.destination == 'Lodge event':
            aLodgeGuests += x.adults
            sLodgeGuests += x.seniors
            kLodgeGuests += x.kids
            dLodgeGuests += x.dogs

        if x.overnight:
            overnights += 1
            if x.cabin:
                aCabins += x.adults
                sCabins += x.seniors
                kCabins += x.kids
                dCabins += x.dogs
            if x.camping:
                aCampers += x.adults
                sCampers += x.seniors
                kCampers += x.kids
                dCampers += x.dogs
        
    print('A total of ', len(entryObjList), ' vehicles')
    if aSum != 0: print(aSum, ' adults')
    if sSum != 0: print(sSum, ' seniors')
    if kSum != 0: print(kSum, ' kids') 
    if dSum != 0: print(dSum, ' dogs')

    print('')
    
    if turnArounds != 0: print(turnArounds, ' vehicles turned around')
    if carPasses != 0: print(carPasses, ' visitors returned')
    if parkEmployees != 0: print(parkEmployees, ' Park Employees entered')
    if deleiveries != 0: print(deleiveries, ' Deleivery trucks entered')

    print('')

    if fPasses != 0: print(fPasses, ' people had a family pass')
    if sPasses != 0: print(sPasses, ' people had a senior pass')
    if iPasses != 0: print(iPasses, ' people had a individual pass')

    totalEventGuests = aEventGuests + sEventGuests + kEventGuests + dEventGuests
    if totalEventGuests != 0:
        print('')
        print(totalEventGuests, ' people came for events at a pavillion')
        if aEventGuests != 0: print(aEventGuests, ' adults')
        if sEventGuests != 0: print(sEventGuests, ' seniors')
        if kEventGuests != 0: print(kEventGuests, ' kids')
        if dEventGuests != 0: print(dEventGuests, ' dogs')

    totalLodgeGuests = aLodgeGuests + sLodgeGuests + kLodgeGuests + dLodgeGuests
    if totalLodgeGuests != 0:
        print('')
        print(totalLodgeGuests, ' people came for events at the lodge')
        if aLodgeGuests != 0: print(aLodgeGuests, ' adults')
        if sLodgeGuests != 0: print(sLodgeGuests, ' seniors')
        if kLodgeGuests != 0: print(kLodgeGuests, ' kids')
        if dLodgeGuests != 0: print(dLodgeGuests, ' dogs')
    
    if overnights != 0:
        print('')
        print(overnights, ' vehicles are staying overnight')
        totalPeopleOvernight = aCabins + sCabins + kCabins + dCabins + aCampers + sCampers + sCampers + dCampers
        print('In the cabins')
        if aCabins != 0: print(aCabins, ' adults')
        if sCabins != 0: print(sCabins, ' seniors')
        if kCabins != 0: print(kCabins, ' kids')
        if dCabins != 0: print(dCabins, ' dogs')
        print('In the campground')
        if aCampers != 0: print(aCampers, ' adults')
        if sCampers != 0: print(sCampers, ' seniors')
        if kCampers != 0: print(kCampers, ' kids')
        if dCampers != 0: print(dCampers, ' dogs')

def start():
    global visitorNumber
    print('If you need help type \"help\"')
    
    manageBackups()

    testMode = False
    visitorNumber = getLastEntryNum()

    buff = deque([])
    while True:
        guestCode = input("\n=========================\nEntry: ")
        guestCode = guestCode.lower()
        guestCode = guestCode.strip()
        if guestCode == "close":
            break
        elif guestCode == '':
            print('No action')
        elif guestCode == "help":
            helpMenu()
        elif guestCode == "test":
            testMode = True
            print('Entering test mode')
        elif guestCode == "end":
            testMode = False
            print('Leaving test mode')
        
        elif guestCode == "undo":
            try:
                d = buff.pop()
                print('Will not record entry: ')
                d.display()
            except IndexError:
                print('Max undo reached!')
        
        else:
            x = Entry()
            x.interp(guestCode)
            x.display()
            if testMode:
                print('\nProgram is in test mode and will not record any data!\n',
                  'to exit test mode and start recording type \"end\"')
            else:
                buff.append(x)
                if len(buff) > 5:
                    record(buff.popleft())

    print('recording last entries')
    while len(buff) > 0:
        record(buff.popleft())
    print('We are on entrie ', visitorNumber)

    
#************************* Program Start *************************

autoStart = input('Press enter to start: ')
if autoStart != 'n':
    start()


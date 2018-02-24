from enum import Enum, auto
import random
from pynput import mouse
import pyautogui

xLocs = [887, 939, 987, 1031, 1078, 1126, 1171, 1222, 1267, 1315, 1358, 1404, 1455]

yLocs = [441, 559, 682, 824, 950]

class MyException(Exception):pass
def on_click(x, y, button, pressed):
    global locations
    if pressed:
        if (button == mouse.Button.right):
            raise MyException(button)
        print(x, y)
        locations.append(y)

def clickButton(part, color):
    pyautogui.moveTo(xLocs[color.value], yLocs[part.value], duration=0.2)
    pyautogui.click()
    

class Part(Enum):
    KNOB = 0
    HANDLE = 1
    RING = 2
    BODY = 3
    TOP = 4

class Color(Enum):
    WHITE = 0
    RED = 1
    YELLOW_P = 2
    ORANGE_P = 3
    RED_P = 4
    PURPLE_P = 5
    BLUE_P = 6
    GREEN_P = 7
    YELLOW = 8
    ORANGE = 9
    PINK = 10
    GREEN = 11
    BLACK = 12

def randAccentColor():
    return random.choice(list(Color))
def randMainColor():
    return random.choice(list(Color)[:-1])

def completeMixUp():
    matchingAccent = random.randrange(0,5)
    matchingMain = random.randrange(0,2)

    if matchingAccent == 0:
        knob = ring = top = randAccentColor()
    elif matchingAccent == 1:
        knob = ring = randAccentColor()
        top = randAccentColor()
    elif matchingAccent == 2:
        knob = top = randAccentColor()
        ring = randAccentColor()
    elif matchingAccent == 3:
        ring = top = randAccentColor()
        knob = randAccentColor()
    else:
        knob = randAccentColor()
        ring = randAccentColor()
        top = randAccentColor()
        
    if matchingMain ==0:
        handle = body = randMainColor()    
    else:
        handle = randMainColor()
        body = randMainColor()

##with mouse.Listener(on_click=on_click) as listener:
##    try:
##        listener.join()
##    except MyException as e:
##        pass
##
##print(locations)
##

#knob = randAccentColor()
handle = ring = top =randMainColor()
body = knob = Color.WHITE

##randAccentColor()
##randMainColor()

print('Knob', knob, sep='\t')
print('Handle', handle, sep='\t')
print('Ring', ring, sep='\t')
print('Body', body, sep='\t')
print('Top', top, sep='\t')

clickButton(Part.KNOB, knob)
clickButton(Part.HANDLE, handle)
clickButton(Part.RING, ring)
clickButton(Part.BODY, body)
clickButton(Part.TOP, top)


    



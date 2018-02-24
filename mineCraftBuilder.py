from pynput.keyboard import Key, Controller
from pynput import keyboard
import time 

# The key combination to check
COMBINATION = {keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.insert}

# The currently active modifiers
current = set()

typer = Controller()

activate = False
on = True

def formatCommand(start, end, block, handle=''):
    output = 'fill '
    for i in range(3):
        output += str(start[i]) + ' '
    for i in range(3):
        output += str(end[i]) + ' '
    output += block + ' '
    output += '0 '
    output += handle
    return output

def executeFillCommand(start, end, block, handle=''):
    typer.press('/')
    typer.release('/')
    time.sleep(0.25)
    typer.type(formatCommand(start, end, block, handle=handle))
    time.sleep(0.25)
    typer.press(Key.enter)
    typer.release(Key.enter)
    time.sleep(0.25)

def build():
    executeFillCommand((-280, 175, 527), (-280+100, 175, 527+100), 'stone', 'replace')
    #180 x 180

def on_press(key):
    global activate
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
            activate = True  
    if key == keyboard.Key.end:
        listener.stop()


def on_release(key):
    global activate
    try:
        current.remove(key)
        if activate and len(current) == 0:
            activate = False
            build()
    except KeyError:
        pass
    

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
    



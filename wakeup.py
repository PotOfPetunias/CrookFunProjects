import time
from datetime import datetime, time
from time import sleep
##from tkinter import*
import tkinter as tk

def getColor(num):
    t = 6 - len(hex(num)[2:])
    s = '#'
    for i in range(t):
        s += '0'
    s += hex(num)[2:]
    return s

def next(num):
    if num >= 0xff0000:
        if num >= 0xffdf00:
            return 0xffdf00
        return num + 0x000100
    
    num = num + 0x010000
    if num > 0x400000:
        num = num + 0x000100
    
    return num
    
def waitUntil(t):
    startTime = time(*(map(int, t.split(':'))))
    while startTime > datetime.today().time(): 
        sleep(1)



animation = tk.Tk()
canvas = tk.Canvas(animation, width=1920, height=1080)
canvas.pack()

num = 0
for x in range(0, 0xfff):
    canvas.configure(bg=getColor(num))
    num = next(num)
    canvas.update()
    sleep(0.2)

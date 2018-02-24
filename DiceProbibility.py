import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random

def roll(num, dnum):
    dice = []
    for i in range(num):
        dice.append(random.randint(1, dnum))
    return dice

def rollSum(times, num, dnum):
    rolls = []
    for i in range(times):
        rolls.append(sum(roll(num,dnum)))
    return rolls

a = plt.figure(1)
# the histogram of the data
n, bins, patches = plt.hist(rollSum(100000,3,6), 50)


plt.xlabel('Dice')
plt.ylabel('Number of times')
plt.title('Dice Spread')
plt.grid(True)

a.show()

b = plt.figure(2)

allrolls = [sum([i,j,k]) for i in range(1,6) for j in range(1,6)  for k in range(1,6)]
print(allrolls)
n, bins, patches = plt.hist(allrolls, 50)

plt.xlabel('Dice')
plt.ylabel('Number of times')
plt.title('Dice Spread')
plt.grid(True)

b.show()

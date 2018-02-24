import matplotlib.pyplot as plt
import random
import time

def plot():
    file = open('solveTimes.txt')
    lines = file.readlines()
    file.close()
    times = []
    for i in range(len(lines)):
        times.append(float(lines[i]))
    print(times)                

    plt.plot(times)
    plt.show()
def getScramble():
    moves = [['R', 'R\'', 'R2', 'L',  'L\'',  'L2'],
             ['U', 'U\'', 'U2', 'D',  'D\'',  'D2'],
             ['F', 'F\'', 'F2', 'B',  'B\'',  'B2']]
             
    scramble = ''
    upOrdown = [1,-1]
    axis = random.choice(range(3))
    for i in range(15):
        scramble = scramble + '  ' + random.choice(moves[axis])
        axis = (axis + random.choice(upOrdown)) %3
    return scramble

print(getScramble())
input('waiting')
start = time.time()
input()
finalTime = time.time() - start
print(finalTime)


##lines[i] = lines[i][1:6]
##print(lines)
##lines[0] = '23.96'
##out = open('solveTimes.txt', 'w')
##for line in lines:
##    out.write(line)
##    out.write('\n')
##out.close()

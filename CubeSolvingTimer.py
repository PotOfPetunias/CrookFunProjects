import matplotlib.pyplot as plt

file = open('solveTimes.txt')
lines = file.readlines()
file.close()
times = []
for i in range(len(lines)):
    times.append(float(lines[i]))
print(times)                

plt.plot(times)
plt.show()

##lines[i] = lines[i][1:6]
##print(lines)
##lines[0] = '23.96'
##out = open('solveTimes.txt', 'w')
##for line in lines:
##    out.write(line)
##    out.write('\n')
##out.close()

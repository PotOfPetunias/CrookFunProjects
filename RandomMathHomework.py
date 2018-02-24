def contains(matrix, frac):
    for f in matrix:
        if frac[0]/frac[1] == f[0]/f[1]:
            return True
    return False

numerator = [[j for j in range(1,28)] for i in range(1,28)]
denominator = [[i for j in range(1,28)] for i in range(1,28)]
y = []
y.append([numerator[0][0], denominator[0][0]])
for x in range(1,10):
    for i in range(0, x+1):
        y.append([numerator[i][x-i], denominator[i][x-i]])
yWithoutDuplicates = []
for fraction in y:
    if not contains(yWithoutDuplicates, fraction):
        yWithoutDuplicates.append(fraction)
        
print(yWithoutDuplicates[27])



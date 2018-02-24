l = [i for i in range(1, 101)]
for i in range(2,100,3):
    l[i] = 'fizz'
for i in range(4,100,5):
    if (i+1)%3 == 0:
        l[i] += 'buzz'
    else:
        l[i] = 'buzz' 
for i in l:
    print(i)

f = open('cubepeople.txt')
lines = f.readlines()
f.close()
onlyspaces = []
past = False
for l in lines:
    ln = l.split('\t')
    for w in ln:
        if ' ' in w:
            onlyspaces.append(w)
dups = []
names = []
for name in onlyspaces:
    if name in names:
        dups.append(name)
    else:
        names.append(name)
        
[print(d) for d in dups]

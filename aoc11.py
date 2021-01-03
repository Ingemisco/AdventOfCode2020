file = open("aoc11.txt")
table = list(map(lambda x: x.replace('\n', ''), file.readlines()))

# part 1
# Arrays sind besser als Listen!
def iterate():
    ntable = []
    for i in range(len(table)):
        ntable.append([])
        for j in range(len(table[i])):
            ntable[i].append(0)
    temp = []
    changed = False
    for i in range (len(table) - 1):
        for j in range(len(table[i]) - 1):
            if table[i][j] == '#':
                ntable[i+1][j+1] += 1
            if table[i+1][j+1] == '#':
                ntable[i][j] += 1
            if table[i+1][j] == '#':
                ntable[i][j+1] += 1
            if table[i][j+1] == '#':
                ntable[i+1][j] += 1
    for i in range (len(table)):
        for j in range(len(table[i]) - 1):
            if table[i][j] == '#':
                ntable[i][j+1] += 1
            if table[i][j+1] == '#':
                ntable[i][j] += 1
    for i in range (len(table)-1):
        for j in range(len(table[i])):
            if table[i][j] == '#':
                ntable[i+1][j] += 1
            if table[i+1][j] == '#':
                ntable[i][j] += 1
    
    for i in range (len(table)):
        temp.append([])
        for j in range(len(table[i])):
            if table[i][j] == 'L' and ntable[i][j] == 0:
                temp[i].append('#')
                changed = True
            elif table[i][j] == '#' and ntable[i][j] >= 4:
                temp[i].append('L')
                changed = True
            else:
                temp[i].append(table[i][j])
            ntable[i][j] = 0
    return temp, changed
    
# part 2

def testdir(i,j, di, dj):
    if i + di >= len(table) or j + dj >= len(table[i]):
        return 0
    if i + di < 0 or j + dj < 0:
        return 0
    if table[i+di][j+dj] == 'L':
        return 0
    if table[i+di][j+dj] == '#':
        return 1
    return testdir(i+di, j+dj, di, dj)
    
def testpos(i, j):
    a = 0
    for p in range(-1,2):
        for q in range(-1,2):
            if p == 0 and q == 0:
                continue
            a += testdir(i,j, p, q)
    return a

def iterate2():
    ntable = []
    for i in range(len(table)):
        ntable.append([])
        for j in range(len(table[i])):
            ntable[i].append(0)
    temp = []
    changed = False

    for i in range(len(table)):
        for j in range(len(table[i])):
            ntable[i][j] = testpos(i,j)
            
    for i in range (len(table)):
        temp.append([])
        for j in range(len(table[i])):
            if table[i][j] == 'L' and ntable[i][j] == 0:
                temp[i].append('#')
                changed = True
            elif table[i][j] == '#' and ntable[i][j] >= 5:
                temp[i].append('L')
                changed = True
            else:
                temp[i].append(table[i][j])
            ntable[i][j] = 0
    return temp, changed

q = True
while(q):
    table, q = iterate2()

sum = 0
for i in range (len(table)):
    for j in range(len(table[i])):
        if table[i][j] == '#':
            sum += 1
print(sum)
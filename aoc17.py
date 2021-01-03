file = open("aoc17.txt")
start = [list(map(lambda x: [char for char in x.replace("\n", "")] , file.readlines()))]

# part 1

def countneighbors(table, x, y, z):
    sx = max(0, x - 1)
    ex = min(len(table[0][0]), x+2)
    sy = max(0, y - 1)
    ey = min(len(table[0]), y+2)
    sz = max(0, z - 1)
    ez = min(len(table), z + 2)
    sum = 0
    for i in range(sz, ez):
        for j in range(sy, ey):
            for k in range(sx, ex):
                if  (i != z or j != y or k != x) and table[i][j][k] == '#':
                    sum += 1
    return sum

def iterate():
    temp = []
    nbs  = []
    for z in range(len(start) + 2):
        temp.append([])
        nbs.append([])
        for y in range(len(start[0]) + 2):
            temp[z].append([])
            nbs[z].append([])
            for x in range(len(start[0][0]) + 2):
                temp[z][y].append('.')
                nbs[z][y].append(0)

    for z in range(len(start)):
        for y in range(len(start[z])):
            for x in range(len(start[z][y])):
                temp[z+1][y+1][x+1] = start[z][y][x]

    for z in range(len(nbs)):
        for y in range(len(nbs[z])):
            for x in range(len(nbs[z][y])):
                nbs[z][y][x] = countneighbors(temp, x,y,z)

    for z in range(len(nbs)):
        for y in range(len(nbs[z])):
            for x in range(len(nbs[z][y])):
                a = nbs[z][y][x]
                if a == 3 or (a == 2 and temp[z][y][x] == '#'):
                    temp[z][y][x] = '#'
                else:
                    temp[z][y][x] = '.'

    return temp

def countactive(table):
    sum = 0
    for i in table:
        for j in i:
            for k in j:
                if k == '#':
                    sum += 1
    return sum


for i in range(6):
    start = iterate()

print(countactive(start))


# part  2

def countneighbors2(table, x, y, z, w):
    sx = max(0, x - 1)
    ex = min(len(table[0][0][0]), x+2)
    sy = max(0, y - 1)
    ey = min(len(table[0][0]), y+2)
    sz = max(0, z - 1)
    ez = min(len(table[0]), z + 2)
    sw = max(0, w - 1)
    ew = min(len(table), w + 2)
    sum = 0
    for h in range(sw, ew):
        for i in range(sz, ez):
            for j in range(sy, ey):
                for k in range(sx, ex):
                    if  (h!= w or i != z or j != y or k != x) and table[h][i][j][k] == '#':
                        sum += 1
    return sum

def iterate2():
    temp = []
    nbs  = []
    for w in range(len(start) + 2):
        temp.append([])
        nbs.append([])
        for z in range(len(start[0]) + 2):
            temp[w].append([])
            nbs[w].append([])
            for y in range(len(start[0][0]) + 2):
                temp[w][z].append([])
                nbs[w][z].append([])
                for x in range(len(start[0][0][0]) + 2):
                    temp[w][z][y].append('.')
                    nbs[w][z][y].append(0)

    for w in range(len(start)):
        for z in range(len(start[w])):
            for y in range(len(start[w][z])):
                for x in range(len(start[w][z][y])):
                    temp[w+1][z+1][y+1][x+1] = start[w][z][y][x]

    for w in range(len(nbs)):
        for z in range(len(nbs[w])):
            for y in range(len(nbs[w][z])):
                for x in range(len(nbs[w][z][y])):
                    nbs[w][z][y][x] = countneighbors2(temp, x, y, z, w)

    for w in range(len(nbs)):
        for z in range(len(nbs[w])):
            for y in range(len(nbs[w][z])):
                for x in range(len(nbs[w][z][x])):
                    a = nbs[w][z][y][x]
                    if a == 3 or (a == 2 and temp[w][z][y][x] == '#'):
                        temp[w][z][y][x] = '#'
                    else:
                        temp[w][z][y][x] = '.'

    return temp

file = open("aoc17.txt")
start = [[list(map(lambda x: [char for char in x.replace("\n", "")] , file.readlines()))]]

def countactive2(table):
    sum = 0
    for i in table:
        for j in i:
            for k in j:
                for l in k:
                    if l == '#':
                        sum += 1
    return sum


for i in range(6):
    start = iterate2()
print(countactive2(start))




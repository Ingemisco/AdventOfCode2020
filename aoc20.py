import re

file = open("aoc20.txt")
ls = filter(lambda x: len(x) > 0, file.read().split("\n\n"))

# part 1

def calc(tile, face):
    n = len(tile) 
    if face == 0: # top
        fct = lambda x: (0, x)
    elif face == 2: #bottom
        fct = lambda x: (n - 1, n - 1 - x)
    elif face == 1: # right
        fct = lambda x: (n - 1 - x, n - 1)
    else: # 3 left
        fct = lambda x: (x, 0)

    val0 = 0
    val1 = 0
    for i in range(n):
        x, y = fct(i)
        if tile[x][y] == '#':
            val0 += 2**i
            val1 += 2**(n - 1 - i)
    if val0 > val1:
        return val0, False
    else:
        return val1, True

tiles = {}
vals = {}

for p in ls:
    q = p.split(':\n')
    id = int(re.search(r"(\d+)", q[0]).group(0))
    tile = q[1].split("\n")
    tiles[id] = tile
    for i in range(4):
        val, flipped = calc(tile, i)
        if val not in vals:
            vals[val] = []
        vals[val].append( (id, i, flipped)  )

borders = list(map( lambda x: x[0], filter( lambda x: len(x) == 1, vals.values() )))

borders.sort(key= lambda x: x[0])

res = 1
for i in range(len(borders) - 1):
    if borders[i][0] == borders[i+1][0]:
        corner = (borders[i], borders[i+1])
        res *= borders[i][0]
        

print(res)


# part 2

def calc2(tile, face):
    n = len(tile) 
    if face == 0: # top
        fct = lambda x: (0, x)
    elif face == 2: #bottom
        fct = lambda x: (n - 1, x)
    elif face == 1: # right
        fct = lambda x: (x, n - 1)
    else: # else 3 =  left
        fct = lambda x: (x, 0)

    val0 = 0
    for i in range(n):
        x, y = fct(i)
        if tile[x][y] == '#':
            val0 += 2**i
    return val0

def flip(id):
    tile = tiles[id]
    n = len(tile)
    m = len(tile[0])

    temp = [[tile[j][m - 1 - i] for i in range(m) ] for j in range(n)]
    tiles[id] = temp

def rotate(id):
    tile = tiles[id]
    n = len(tile)
    m = len(tile[0])

    temp = [[tile[m - 1 - i][j] for i in range(m)] for j in range(n)]
    tiles[id] = temp

def other(l, val):
    for i in l:
        if i[0] != val:
            return i[0]

def match(id0, side0, id1, side1):
    for _ in range(4):
        if calc2(tiles[id0], side0) == calc2(tiles[id1], side1):
            return
        rotate(id1)

    flip(id1)

    for _ in range(4):
        if calc2(tiles[id0], side0) == calc2(tiles[id1], side1):
            return
        rotate(id1)
    
arr = {}

for i in range(4):
    if {(corner[0][1] + i)  % 4, (corner[1][1] + i ) % 4} == {0, 3}:
        id = corner[0][0]
        arr[0,0] = id
        for _ in range(i):
            rotate(id)
        break 

i = 1
j = 0

while True:
    tile = arr[(j, i-1)]
    rightval = calc(tiles[tile], 1)[0]
    nexttile = other(vals[rightval], tile)

    if nexttile != None:
        match(tile, 1, nexttile, 3)
        arr[(j,i)] = nexttile
        i += 1
    else:
        up = arr[(j, 0)]
        j += 1
        i = 1
        upval = calc(tiles[up], 2)[0]
        downtile = other(vals[upval], up)
        
        if downtile != None:
            match(up, 2, downtile, 0)
            arr[(j,0)] = downtile
        else:
            break   

picture = [  [ tiles[arr[(j // 8, i // 8)]][1 + (j % 8)][1 + (i % 8)] for i in range(96)] for j in range(96) ]

temp = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster = []
for j in range(len(temp)):
    for i in range(len(temp[j])):
        if temp[j][i] == '#':
            monster.append((j,i))

water = set()
rough = set()

for j, y in enumerate(picture):
    for i, x in enumerate(y):
        if x == '#':
            water.add((j,i))

def test(n, m):  
    for j in range(len(picture) - n):
        for i in range(len(picture[0]) - m):
            for y, x in monster:
                if picture[j + y][i + x] != '#':
                    break
            else:
                for y, x in monster:
                    rough.add((j + y, i + x))

for t in range(5):
    if t == 2:
        monster = [(j, 19 - i) for (j,i) in monster]
    else:
        test(3, 20)
        monster = [(i, 2 - j ) for (j,i) in monster]
        test(20, 3)
        monster = [(i, 19 - j) for (j,i) in monster]

print(len(water.difference(rough)))

file = open("aoc24.txt")

ls = file.readlines()


tiles = {}

def getpos(line):
    e = 0
    ne = 0

    while len(line) > 0:
        if line.startswith('e'):
            e += 1 
        elif  line.startswith('w'):
            e -= 1
        elif line.startswith('n'):
            line = line[1:]
            if line.startswith('e'):
                ne += 1
            elif  line.startswith('w'):
                e -= 1
                ne += 1
        else:
            line = line[1:]
            if line.startswith('e'):
                e += 1
                ne -= 1
            elif  line.startswith('w'):
                ne -= 1
        line = line[1:]

    return e, ne

for s in ls:
    e, ne = getpos(s)
    if (e, ne) not in tiles:
        tiles[(e,ne)] = True
    else:
        tiles[(e,ne)] = not tiles[(e,ne)]

sum = 0
for i in tiles.values():
    if i:
        sum += 1
print(sum)

# part 2

file = open("aoc24.txt")

# file = open("t.txt")

ls = file.readlines()

tiles = {}

for s in ls:
    e, ne = getpos(s)   
    if (e, ne) not in tiles:
        tiles[(e,ne)] = True
    else:
        tiles[(e,ne)] = not tiles[(e,ne)]

adj = [ (-1,0), (-1,1), (0,1), (1, 0), (1, -1), (0, -1)  ]

def next(tiles):
    temp = {}

    for (e, ne), i in tiles.items():
        if i: # True = black, False = white
            for (p, q) in adj:
                if (e + p, ne + q) not in temp:
                    temp[(e + p, ne + q)] = 1
                else:
                    temp[(e + p, ne + q)] += 1

    for (e, ne) in tiles.keys():
        if (e, ne) not in temp:
            temp[e, ne] = 0

    for (e, ne), v in temp.items():
        if (e, ne) in tiles:
            if tiles[(e, ne)]:
                #print(e, ne, tiles[e, ne], v)
                if v == 0 or v > 2:
                    tiles[(e, ne)] = False
            else:
                if v == 2:
                    tiles[(e, ne)] = True
        else: # is white 
            if v == 2:
                tiles[(e, ne)] = True

    return tiles

def blacksum(tiles):
    sum = 0
    for i in tiles.values():
        if i:
            sum += 1
    return sum    


print(blacksum(tiles))
for i in range(100):
    tiles = next(tiles)
print(blacksum(tiles))
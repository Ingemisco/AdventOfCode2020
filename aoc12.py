import math

file = open("aoc12.txt")

ls = ["F10",
"N3",
"F7",
"R90",
"F11"]
ls = file.readlines()
# part 1
posx = 0 # x > 0 => east, x < 0 => west
posy = 0 # y > 0 => north, y < 0 => south
dir  = 0 # dir = 0 => facing east, dir = 90 => facing north, ...

for i in ls:
    c = i[0]
    n = int(i[1:])

    if c == 'R':
        dir -= n
        dir = (dir + 360) % 360
    elif c == 'L':
        dir += n
        dir = (dir + 360) % 360
    elif c == 'F':
        posx += n * math.cos(dir / 180 * math.pi)
        posy += n * math.sin(dir / 180 * math.pi)
    elif c == 'N':
        posy += n
    elif c == 'S':
        posy -= n
    elif c == 'E':
        posx += n
    elif c == 'W':
        posx -= n

print(posx, posy, abs(posx) + abs(posy))


# part 2

posx = 0
posy = 0

wayx = 10
wayy = 1 

for i in ls:
    
    c = i[0]
    n = int(i[1:])
    if c == 'R' or c == 'L': # I miss switch/case
        if (n == 90 and c == 'L') or (n == 270 and c == 'R'): 
            wayx, wayy = -wayy, wayx
        elif (n == 90 and c == 'R') or (n == 270 and c == 'L'): 
            wayx, wayy =   wayy, -wayx
        else:
            wayx = - wayx
            wayy = - wayy
    elif c == 'F':
        posx += wayx * n
        posy += wayy * n
    elif c == 'N':
        wayy += n
    elif c == 'S':
        wayy -= n
    elif c == 'E':
        wayx += n
    elif c == 'W':
        wayx -= n

print(posx, posy, abs(posx) + abs(posy))
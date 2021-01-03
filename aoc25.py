card = 9232416
door = 14144084

#card = 5764801
#door = 17807724

def transform( subject, loop ):
    r = 1
    for _ in range(loop):
        r = r * subject
        r = r % 20201227

    return r

def getloopsize( num ):
    l = 0
    r = 1
    while r != num:
        r = r * 7
        r = r % 20201227
        l += 1
    return l

cl = getloopsize(card)
dl = getloopsize(door)

print(transform(card, dl))
print(transform(door, cl))

# no part 2
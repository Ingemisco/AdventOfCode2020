file = open("aoc22.txt")
ls = file.read().split("\n\n")

p1 = list(map(int, ls[0].split("\n")[1:]))
p2 = list(map(int, ls[1].split("\n")[1:]))

# part 1

def nextturn(p1, p2):
    
    a = p1[0]
    b = p2[0]

    p1 = p1[1:]
    p2 = p2[1:]

    if a > b:
        p1 = p1 + [a, b]
    else:
        p2 = p2 + [b, a]
    return p1, p2

while len(p1) != 0 and len(p2) != 0:
    p1, p2 = nextturn(p1, p2)

sum1 = 0
for i in range(len(p1)):
    sum1 += p1[i] * (len(p1) - i )

sum2 = 0
for i in range(len(p2)):
    sum2 += p2[i] * (len(p2) - i )

print(sum1, sum2)

# part 2

file = open("aoc22.txt")
ls = file.read().split("\n\n")

p1 = list(map(int, ls[0].split("\n")[1:]))
p2 = list(map(int, ls[1].split("\n")[1:]))

max = -1
for i in p1:
    if i > max:
        max = i
for i in p2:
    if i > max:
        max = i
    
def value(player):
    val = 0
    for i, c in enumerate(player):
        val += (max**i) * c
    return val

def game(p1, p2):
    prev = set()
    winner = None
    while len(p1) > 0 and len(p2) > 0:
        p1, p2, prev, winner = nextturn2(p1, p2, prev)
        if winner != None:
            break
    if winner == None:
        if len(p1) == 0:
            winner = False
        elif len(p2) == 0:
            winner = True
    return winner, p1, p2 # True = player 1, False = player 2


def nextturn2(p1, p2, prev):
    p = value(p1)
    q = value(p2)

    if (True, p) in prev or (False, q) in prev:
        return p1, p2, None, True 
    else:
        prev.add( (True, p) )
        prev.add( (False, q) )
    a = p1[0]
    b = p2[0]

    p1 = p1[1:]
    p2 = p2[1:]

    if a <= len(p1) and b <= len(p2):
        winner, s, t = game(p1[:a], p2[:b])
        if winner:
            p1 = p1 + [a, b]
        else:
            p2 = p2 + [b, a]
    else:
        if a > b:
            p1 = p1 + [a, b]
        else:
            p2 = p2 + [b, a]
    return p1, p2, prev, None

winner, p1, p2 = game(p1, p2)
print(p1, p2, winner)

sum1 = 0
for i in range(len(p1)):
    sum1 += p1[i] * (len(p1) - i )

sum2 = 0
for i in range(len(p2)):
    sum2 += p2[i] * (len(p2) - i )

print(sum1, sum2)
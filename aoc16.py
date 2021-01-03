import re

file = open("aoc16.txt", "r")
temp = file.read().split("\n\n")
restrictions = temp[0].split("\n")
yourticket = temp[1].split("\n")[1]
yourticket = yourticket.split(",")
tickets = list(filter(lambda x: len(x) > 0 and re.match(r"\d", x), temp[2].split("\n")))

# part 1

restrs = []
for s in restrictions:
    restrs += list(map( lambda x: tuple(map(int, x.split("-"))), re.findall(r"\d+-\d+", s)))

def fitsany(val):
    for (p, q) in restrs:
        if p <= val <= q:
            return True
    return False 

tickets = list(map(lambda x: list(map(int, x.split(","))), tickets))

sum = 0
for i in tickets:
    for j in i:
        if not fitsany(j):
            sum += j

print(sum)

# part 2

def fits(l, val):
    for (p, q) in l:
        if p <= val <= q:
            return True
    
    return False 

valid = []

for i in tickets:
    for j in i:
        if not fitsany(j):
            break
    else:
        valid.append(i)

restrs = {}
possible = {}

for r in restrictions:
    t = r.split(":")
    restrs[t[0]] = list(map( lambda x: tuple(map(int, x.split("-"))), re.findall(r"\d+-\d+", t[1])))

for j in restrs:
    possible[j] = []
for i in range(len(valid[0])):
    for (j, k) in restrs.items():
        for l in valid:
            if not fits(k, l[i]):
                break
        else:
            possible[j].append(i)

temp = [(p,q) for p, q in possible.items()]
temp.sort(key = lambda x: len(x[1]))

for i in range(len(temp) - 1):
    for j in range(i + 1, len(temp)):
        if temp[i][1][0] in temp[j][1]:
            temp[j][1].remove(temp[i][1][0])

res = 1
for i in temp:
    if i[0].startswith("departure "):
        a = i[1][0]
        b = yourticket[a]
        res *= int(b)
print(res)
import re

file = open("aoc19.txt")
temp = file.read().split("\n\n")

rulestemp = temp[0].split("\n")
data = temp[1].split("\n")

# part 1

rules = {}

for r in rulestemp:
    t = r.split(":")
    a = int(t[0])
    b = list(map(lambda x: x.split(), t[1].split("|")))
    for i in range(len(b)):
        for j in range(len(b[i])):
            if re.match(r"\d+", b[i][j]):
                b[i][j] = int(b[i][j])
            else:
                b[i][j] = b[i][j].replace("\"", "")
    rules[a] = b

def fitsrule(s, r):
    if len(s) == len(r) == 0:
        return True
    if len(r) > len(s) or len(r) == 0:
        return False
    if not isinstance(r[0], str):
        a = r[0]
        for p in rules[a]:
            if fitsrule(s, p + r[1:]):
                return True
        return False
    else:
        if r[0] == s[0]:
            return fitsrule(s[1:], r[1:])
        else:
            return False
        
sum = 0
for d in data:
    if fitsrule(d, [0]):
        sum += 1
print(sum)

# part 2

rules[8] = [[42], [42, 8]]
rules[11] = [[42,31], [42,11,31]]

sum = 0
for d in data:
    if fitsrule(d, [0]):
        sum += 1
print(sum)
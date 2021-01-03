import re

file = open("aoc04.txt")
input = file.read()

# part 1
ls = input.split("\n\n")

for l in ls:
    re.sub(r"\s+", " ", l)
    #l.replace('\n', ' ')

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
sum = 0
for l in ls:
    b = True
    for s in required:
        if s not in l:
            b = False
    if b:
        sum = sum +1
print(sum)

# part 2

def valid(p):
    d = {}
    templist = p.split()
    for t in templist:
        a = t.split(":")
        d[a[0]] = a[1]
    if not (1920 <= int(d["byr"]) <= 2002 ):
        return False
    if not (2010 <= int(d["iyr"]) <= 2020 ):
        return False
    if not (2020 <= int(d["eyr"]) <= 2030 ):
        return False
    if d["hgt"].endswith("cm"):
        h = int(d["hgt"][:-2])
        if not (150 <= h <= 193):
            return False
    elif d["hgt"].endswith("in"):
        h = int(d["hgt"][:-2])
        if not (59 <= h <= 76):
            return False
    else:
        return False
    if re.match(r"#[0-9a-f]{6}", d["hcl"]) is None:
        return False
    if d["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if re.match(r"^\d{9}$", d["pid"]) is None:
        return False
    return True


sum = 0
for l in ls:
    b = True
    for s in required:
        if s not in l:
            b = False
    if b and valid(l):
        sum = sum + 1
print(sum)
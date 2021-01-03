import re

file = open("aoc06.txt")
input = file.read()
ls = input.split("\n\n")

# part 1

sum = 0
for s in ls:
    a = set()
    for c in s:
        if re.match(r"[a-z]", c):
            a.add(c)
    sum += len(a)
print(sum)


# part 2

sum = 0
for s in ls:
    t = s.split("\n")
    for p in t:
        if p == "":
            t.remove(p)
    for c in "abcdefghijklmnopqrstuvwxyz":
        for p in t:
            if c not in p:
                break
        else:
            sum += 1
print(sum)

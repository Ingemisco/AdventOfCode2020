import re

file = open("aoc14.txt")
ls = file.readlines()


# part 1

def applymask(mask, val):
    res = 0
    for i in range(len(mask)):
        if mask[-i-1] == '1':
            res += 1<<i
        elif mask[-i-1] == 'X':
            res += (val & 1) << i
        val = val >> 1
    return res


mem = {}
mask = ""

for i in ls:
    if i.startswith("mask"):
        mask = re.search(r"[01X]{36}$", i).group(0)
    else:
        adr = int(re.search(r"\[(\d+)\]", i).group(1))
        val = int(re.search(r" (\d+)$", i).group(0))
        mem[adr] = applymask(mask, val)

sum = 0
for (p,q) in mem.items():
    sum += q

print(sum)


# part 2

mem = {}
mask = ""

def adresslist(mask, val):
    res = [0]
    for i in range(len(mask)):
        if mask[-i-1] == '1':
            for j in range(len(res)):
                res[j] += 1 << i
        elif mask[-i-1] == '0':
            for j in range(len(res)):
                res[j] += (val & 1) << i
        else:
            l = len(res)
            for j in range(l):
                res.append(res[j] + (1 << i))
        val = val >> 1
    return res

for i in ls:
    if i.startswith("mask"):
        mask = re.search(r"[01X]{36}$", i).group(0)
    else:
        adr = int(re.search(r"\[(\d+)\]", i).group(1))
        val = int(re.search(r" (\d+)$", i).group(0))
        for l in adresslist(mask, adr):
            mem[l] = val

sum = 0
for (p,q) in mem.items():
    sum += q

print(sum)
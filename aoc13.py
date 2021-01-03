file = open("aoc13.txt")
ls = file.readlines()

time = int(ls[0])

t0 = ls[1].split(",")
t1 = filter(lambda x: x != "x", t0)
t2 = map(int, t1)
dep = list(t2)
print(dep)

p = dep[0]
q = ((time - 1) // p) * (p + 1)

for i in dep:
    if ((time - 1) // i + 1) * i < q:
        p = i
        q = ((time - 1) // p + 1) * p

print(p, q , p * ( q- time ))


# part 2
file = open("aoc13.txt")
ls = file.readlines()

l = []
for i, s in enumerate(ls[1].split(",")):
    if s != "x":
        l.append((i, int(s)))

p = l[0][1]
r = 0
for t in l[1:]:
    a, b = t
    for i in range(b):
        if (p * i + a + r ) % b == 0:
            r = p * i + r
            break
    p = p * b
print(p, r)


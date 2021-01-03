import re

file = open("aoc02.txt")
input = file.readlines()
input = list(map(lambda x: re.sub(":", "", x), input))
ls = list(map(lambda x: re.sub("-", " ", x), input))

# part 1
sum = 0
for s in ls:
    temp = s.split()
    a = int(temp[0])
    b = int(temp[1])
    c = temp[2]
    pwd = temp[3]
    if a <= pwd.count(c) <= b:
        sum = sum + 1
print(sum)


# part 2
sum = 0
for s in ls:
    temp = s.split()
    a = int(temp[0])
    b = int(temp[1])
    c = temp[2]
    pwd = temp[3]
    if (pwd[a-1] == c) ^ (pwd[b-1] == c):
        sum = sum + 1
print(sum)
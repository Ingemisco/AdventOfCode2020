file = open("aoc09.txt")
ls = list(map(int, file.readlines()))

# part 1

for i in range(25, len(ls)):
    b = True
    for j in range(i - 25, i):
        for k in range(j, i):
            if ls[j] + ls[k] == ls[i]:
                b = False
                break
    if b:
        n = i
        print(i, ls[i]) # -> index 582 is result

# part 2

for i in range(n):
    sum = 0
    j = i
    while sum < ls[n]:
        sum += ls[j]
        j += 1
    if sum == ls[n]:
        max = -1
        min = ls[n]
        for k in range(i, j):
            if ls[k] > max:
                max = ls[k]
            if ls[k] < min:
                min = ls[k]

        print(i, j, min + max)


        

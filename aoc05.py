file = open("aoc05.txt")
ls = file.readlines()

def seat_id(r, c):
    return 8 * r + c

def seat_id2(t):
    a,b = t
    return seat_id(a,b)

def position(s):
    a = s[:7]
    b = s[7:10]

    row = 0
    col = 0

    for c in a:
        row *= 2
        if c == 'B':
            row += 1
    for c in b:
        col *= 2
        if c == 'R':
            col += 1
    return (row, col)

# part 1

max = -1
for s in ls:
    a, b = position(s)
    val = seat_id(a, b)
    if val > max:
        max = val   
print(max)

# part 2

ids = [ seat_id2(position(s)) for s in ls ]
ids.sort()

for i in range(len(ids)-1):
    if ids[i] + 1 != ids[i+1]:
        print(ids[i], ids[i+1], ", ", ids[i] + 1, " is missing")


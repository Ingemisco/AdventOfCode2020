file = open("aoc03.txt")
input = file.readlines()

# part 1
sum = 0
for i, l in enumerate(input):
    if l[ ( 3 * i  ) % 31] == '#':
        sum = sum + 1
print(sum)

# part 2

def iter_slope(n, m):
    sum = 0
    for i in range( 0, len(input),m):
        l = input[i]
        if l[ ( n * i // m  ) % 31] == '#':
            sum = sum + 1
    return sum

a = iter_slope(1, 1)
b = iter_slope(3, 1)
c = iter_slope(5, 1)
d = iter_slope(7, 1)
e = iter_slope(1, 2)

print(a, b, c, d, e, a * b * c * d * e)




file = open("aoc10.txt")
ls = list(map(int, file.readlines()))
ls.sort()

# part 1

sum1 = 0
sum3 = 1
if ls[0] == 1:
    sum1 += 1
elif ls[0] == 3:
    sum3 += 1
for i in range(len(ls)-1):
    if ls[i+1] - ls[i] == 1:
        sum1 += 1
    elif ls[i+1] - ls[i] == 3:
        sum3 += 1 
print(sum1, sum3 , sum1 * sum3)

# part 2

n = max(ls)
temp = [0] * (n + 3 )
i = n - 1
temp[n] = 1
temp[n+1] = 0
temp[n+2] = 0
j = len(ls) - 2
while i > 0:
    if i == ls[j]:
        temp[i] = temp[i+1] + temp[i+2] + temp[i+3]
        j -= 1
        i -= 1
    else:
        temp[i] = 0
        i -= 1
temp[0] = temp[1] + temp[2] + temp[3]
print(temp[0])
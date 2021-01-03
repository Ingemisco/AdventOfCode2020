file = open("aoc01.txt", "r")
nums = list(map(int, file.readlines()))

# part 1
l = len(nums)
for i in range(l - 1):
    for j in range(i + 1, l):
        p = nums[i]
        q = nums[j]
        if p + q == 2020:
            print(p, q, p * q)

# part 2
for i in range(l -2):
    for j in range(i + 1, l - 1):
        for k in range(j + 1, l):
            p = nums[i]
            q = nums[j]
            r = nums[k]
            if p + q + r  == 2020:
               print(p, q, r, p * q * r)

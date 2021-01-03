ls = [0,3,1,6,7,5]

# part 1 and 2

nums = {}
for i,j in enumerate(ls[:-1]):
    nums[j] = i

lastnum = ls[-1]

for i in range(len(ls),30000000):
    if lastnum in nums:
        p = nums[lastnum]
        nums[lastnum] = i - 1
        lastnum = i - 1 - p
    else:
        p = 0
        nums[lastnum] = i - 1
        lastnum = 0

print(lastnum)
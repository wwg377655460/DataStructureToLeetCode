nums = [1, 3, 6, 8, 12]
min = 1000

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if min > nums[i] + nums[j]:
            min = nums[i] + nums[j]

print(min)

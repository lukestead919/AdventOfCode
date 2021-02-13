f = open("DataFiles/10.txt")
nums = sorted([int(l) for l in f.read().splitlines()])
nums.insert(0, 0)
nums.append(max(nums) + 3)
print(nums)
print(zip(nums, nums[1:]))

diff = [t - s for s, t in zip(nums, nums[1:])]

print(diff.count(1) * diff.count(3))

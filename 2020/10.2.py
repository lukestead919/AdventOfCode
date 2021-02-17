f = open("DataFiles/10.txt")
nums = sorted([int(l) for l in f.read().splitlines()])
nums.insert(0, 0)
nums.append(max(nums) + 3)

chainsFromPosition = [0]*len(nums)
chainsFromPosition[-1] = 1
def populateNumberOfChainsFromPosition(i):
    currentNum = nums[i]
    chains = 0
    for j in range(i+1, min(i+4, len(nums))):
        if nums[j] - currentNum <= 3:
            chains += chainsFromPosition[j]
    chainsFromPosition[i] = chains

for i in range(len(nums)-2, -1, -1):
    populateNumberOfChainsFromPosition(i)

print(chainsFromPosition[0])

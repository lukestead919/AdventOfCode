import sys
f = open("DataFiles/9.txt")
nums = [int(l) for l in f.read().splitlines()]


sum = 1212510616

for i in range(len(nums)):
    runningTotal = nums[i]
    for j in range(i+1, len(nums)):
        runningTotal += nums[j]
        if runningTotal > sum:
            # print(i, i+j, runningTotal)
            break
        elif runningTotal == sum:

            contiguousRange = nums[i:j]
            print(min(contiguousRange) + max(contiguousRange))
            sys.exit()

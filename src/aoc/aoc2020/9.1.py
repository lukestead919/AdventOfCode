import sys
f = open("DataFiles/9.txt")
nums = [int(l) for l in f.read().splitlines()]

previous = 25


def sumOfPrevious(i):
    for j in range(i-previous, i):
        for k in range(j+1, i):
            if nums[j] + nums[k] == nums[i]:
                return True

    return False


for i in range(previous, len(nums)):
    if not sumOfPrevious(i):
        print(nums[i])
        sys.exit()

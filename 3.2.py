from numpy import prod

def calculateTreesForSlope(rightStep, downStep):
    f = open("DataFiles/3.txt")
    input = f.read().splitlines()

    retval = 0
    tree = "#"
    down = 0
    right = 0
    while down < len(input):
        if input[down][right % len(input[down])] == tree:
            retval += 1
        down += downStep
        right += rightStep

    print(retval)
    return retval

ans = []

ans.append(calculateTreesForSlope(1, 1))
ans.append(calculateTreesForSlope(3, 1))
ans.append(calculateTreesForSlope(5, 1))
ans.append(calculateTreesForSlope(7, 1))
ans.append(calculateTreesForSlope(1, 2))

print(ans, prod(ans))


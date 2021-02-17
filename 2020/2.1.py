f = open("DataFiles/2.txt")
input = f.read().splitlines()

retval = 0

for i in input:
    split = i.split(" ")
    bounds = [int(i) for i in split[0].split("-")]
    char = split[1][0]
    password = split[2]

    # print(i, split, bounds, char, password)

    countOfChar = password.count(char)
    if countOfChar >= bounds[0] and countOfChar <= bounds[1]:
        retval += 1


print(retval)
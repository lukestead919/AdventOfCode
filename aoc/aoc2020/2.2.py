f = open("DataFiles/2.txt")
input = f.read().splitlines()

retval = 0

for i in input:
    split = i.split(" ")
    positions = [int(i)-1 for i in split[0].split("-")]
    char = split[1][0]
    password = split[2]

    # print(i, split, bounds, char, password)
    # print(password[positions[0]] == char, password[positions[1]] == char)

    if bool(password[positions[0]] == char) ^ bool(password[positions[1]] == char):
        retval += 1


print(retval)

f = open("DataFiles/3.txt")
input = f.read().splitlines()

retval = 0
tree = "#"
for i in range(len(input)):
    if input[i][3*i % len(input[i])] == tree:
        retval += 1

print(retval)
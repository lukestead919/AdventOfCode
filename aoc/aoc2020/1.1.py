f = open("DataFiles/1.txt")
input = f.read().splitlines()
input = [int(i) for i in input]
input.sort()

sum = 2020

print(input)
for i in input:
    for j in input:
        if i+j == sum:
            print(i, j, i*j)

        if i+j > sum:
            break

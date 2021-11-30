f = open("DataFiles/1.txt")
input = f.read().splitlines()
input = [int(i) for i in input]
input.sort()

sum = 2020

print(input)
for i in input:
    for j in input:
        for k in input:
            if i+j+k == sum:
                print(i, j, k, i*j*k)

            if i+j+k>sum:
                break
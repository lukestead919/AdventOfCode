seatNums = []
with open("DataFiles/5.txt") as f:
    for line in f:
        binLine = line.replace("F", "0").replace(
            "B", "1").replace("L", "0").replace("R", "1")
        seatNums.append(int(binLine, 2))

seatNums.sort()
for i in range(len(seatNums) -1):
    if seatNums[i] + 2 == seatNums[i+1]:
        print(seatNums[i] + 1)
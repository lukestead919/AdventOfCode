maxSeatNum = 0
with open("DataFiles/5.txt") as f:
    for line in f:
        # print(line)
        binLine = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        # print(binLine)
        seatNum = int(binLine, 2)
        maxSeatNum = max(maxSeatNum, seatNum)

print(maxSeatNum)

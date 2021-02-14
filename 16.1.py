def isInAnyRange(validRanges, v):
    for range in validRanges:
        range = [int(r) for r in range.split("-")]
        if v >= range[0] and v <= range[1]:
            return True
    return False


with open("DataFiles/16.txt") as f:
    lines = f.read().split("\n\n")
    fields = lines[0].split("\n")
    myTicket = lines[1].split("\n")
    otherTickets = lines[2].split("\n")

    # print(fields)
    # print(myTicket)
    # print(otherTickets)
validRanges = []
for field in fields:
    validRanges += (field[field.find(":") + 2:].split(" or "))

retval = 0
print(validRanges)
for t in otherTickets:
    values = [int(v) for v in t.split(",")]
    for v in values:
        if not isInAnyRange(validRanges, v):
            retval += v
            print(v)


print(retval)

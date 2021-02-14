def isInAnyRange(validRanges, v):
    for range in validRanges:
        range = [int(r) for r in range.split("-")]
        if v >= range[0] and v <= range[1]:
            return True
    return False


def isValidTicket(validRanges, t):
    for v in t:
        if not isInAnyRange(validRanges, v):
            return False
    return True


with open("DataFiles/16.txt") as f:
    lines = f.read().split("\n\n")
    fields = lines[0].split("\n")
    myTicket = [int(t) for t in lines[1].split(",")]
    otherTickets = [[int(t) for t in ticket.split(",")]
                    for ticket in lines[2].split("\n")]

    # print(fields)
    # print(myTicket)
    # print(otherTickets)

validRanges = dict()
for field in fields:
    validRanges[field[:field.find(":")]] = (
        field[field.find(":") + 2:].split(" or "))

allValidRanges = [range for ranges in validRanges.values() for range in ranges]
# print(allValidRanges)


validTickets = []
for t in otherTickets:
    if isValidTicket(allValidRanges, t):
        validTickets.append(t)
# print(validTickets)
# print(validTickets[0])
# print(validTickets[0][0])
columnValues = [[validTickets[i][j]
                 for i in range(len(validTickets))] for j in range(len(validTickets[0]))]

# now, for each field, go through each of the columns on the valid ticket and find the columns where all the values are in the ranges for that field
validColsForField = {}

for field, ranges in validRanges.items():
    print(field, ranges)
    validColsForField.setdefault(field, [])
    for index, col in enumerate(columnValues):
        if all(isInAnyRange(ranges, val) for val in col):
            # print(field, "\n", ranges, "\n", index, "\n", col)
            validColsForField[field].append(index)

print(validColsForField)

validFieldsForCols = {}
for i in range(20):
    validFieldsForCols.setdefault(i, [])
    for field, cols in validColsForField.items():
        if i in cols:
            validFieldsForCols[i].append(field)

for e, val in validColsForField.items():
    print(e, val)

print("\n\n")
for e, val in validFieldsForCols.items():
    print(e, val)

#just decided to do the rest by hand, would take longer to code
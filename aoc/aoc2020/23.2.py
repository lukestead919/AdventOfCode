from os import link


with open("DataFiles/23.txt") as f:
    order = [int(a) for a in f.read()]

order = [order[i] if i < 9 else i+1 for i in range(1000000)]


def makeMove(linkedList, currentValue):
    x = linkedList[currentValue]
    y = linkedList[x]
    z = linkedList[y]
    afterz = linkedList[z]

    destinationNumber = currentValue - 1
    if destinationNumber == 0:
        destinationNumber = len(linkedList)
    while destinationNumber in [x, y, z]:
        destinationNumber += -1
        if destinationNumber == 0:
            destinationNumber = len(linkedList)

    afterDestination = linkedList[destinationNumber]

    linkedList[currentValue] = afterz
    linkedList[destinationNumber] = x
    linkedList[z] = afterDestination
    return afterz


currentValue = order[0]
linkedList = {}
for a, b in zip(order, order[1:] + [order[0]]):
    linkedList[a] = b

for i in range(10000000):
    # make a singly linked list
    if not i % 100000:
        print(i)
    currentValue = makeMove(linkedList, currentValue)

print(linkedList[1]*linkedList[linkedList[1]])

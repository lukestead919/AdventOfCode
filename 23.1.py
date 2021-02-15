with open("DataFiles/23.txt") as f:
    order = [int(a) for a in f.read()]

currentIndex = 0


def makeMove():
    global currentIndex, order
    currentNumber = order[currentIndex]
    loop = order + order
    cupsToMove = loop[currentIndex+1:currentIndex+4]
    o = loop[currentIndex+4:currentIndex+10]

    try:
        destination = max([l for l in o if l < currentNumber])
    except:
        destination = max([l for l in o])

    destinationIndex = o.index(destination)

    order = o[:destinationIndex+1] + cupsToMove + o[destinationIndex+1:]
    currentIndex = (order.index(currentNumber) + 1) % 9


for i in range(100):
    makeMove()

print(order)

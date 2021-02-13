with open("DataFiles/12.txt") as f:
    commands = f.read().splitlines()

waypointN = 1
waypointE = 10
north = 0
east = 0

def rotateWaypointClockwise90():
    global waypointN, waypointE
    waypointN, waypointE = -waypointE, waypointN


def rotateWaypointClockwise(numberOfTimes):
    for i in range(numberOfTimes):
        rotateWaypointClockwise90()


def rotateWaypointAntiClockwise(numberOfTimes):
    for i in range(4-numberOfTimes):
        rotateWaypointClockwise90()

for cmd in commands:
    d = cmd[0]
    m = int(cmd[1:])

    if d == "N":
        waypointN += m
    elif d == "E":
        waypointE += m
    elif d == "S":
        waypointN -= m
    elif d == "W":
        waypointE -= m
    elif d == "L":
        rotateWaypointAntiClockwise(m//90)
    elif d == "R":
        rotateWaypointClockwise(m//90)
    elif d == "F":
        north += m * waypointN
        east += m * waypointE
    else:
        print("d is " + str(d))


print(north, east)
print(abs(north) + abs(east))

with open("DataFiles/12.txt") as f:
    commands = f.read().splitlines()

north = 0
east = 0
direction = 90  # in degrees

for cmd in commands:
    d = cmd[0]
    m = int(cmd[1:])

    if d == "F":
        if direction == 0:
            d = "N"
        elif direction == 90:
            d = "E"
        elif direction == 180:
            d = "S"
        elif direction == 270:
            d = "W"
        else:
            print(str(direction) + " is the current direction")

    if d == "N":
        north += m
    elif d == "E":
        east += m
    elif d == "S":
        north -= m
    elif d == "W":
        east -= m
    elif d == "L":
        direction -= m
    elif d == "R":
        direction += m
    else:
        print("d is " + str(d))

    direction = direction % 360

print(north, east)
print(abs(north) + abs(east))

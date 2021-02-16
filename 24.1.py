# convert e and w into nese and nwsw respectively. This gives us a coordinate system with unit vectors of ne and nw, and sw = - ne and se = -nw

with open("DataFiles/24.txt") as f:
    lines = f.read().splitlines()

blackTiles = []

for line in lines:
    nw = 0
    ne = 0
    while len(line) > 0:
        if line[0] == "e":
            ne += 1
            nw += -1
            line = line[1:]
        elif line[0] == "w":
            ne += -1
            nw += 1
            line = line[1:]
        elif line[0:2] == "ne":
            ne += 1
            line = line[2:]
        elif line[0:2] == "nw":
            nw += 1
            line = line[2:]
        elif line[0:2] == "se":
            nw += -1
            line = line[2:]
        elif line[0:2] == "sw":
            ne += -1
            line = line[2:]

    if (nw, ne) in blackTiles:
        blackTiles.remove((nw, ne))
    else:
        blackTiles.append((nw, ne))

print(len(blackTiles))

import numpy as np

with open("DataFiles/20.txt") as f:
    tiles = f.read().split("\n\n")
    print(tiles[0])

tilesDict = {}
tileEdges = {}
for tile in tiles:
    tile = tile.splitlines()
    num = tile[0][5:-1]
    tile = np.array([[c for c in line] for line in tile[1:]])
    tilesDict[num] = tile

    edges = []
    edges.append(tile[0, :])
    edges.append(tile[-1, :])
    edges.append(tile[0, 10::-1])
    edges.append(tile[-1, 10::-1])

    edges.append(tile[:, 0])
    edges.append(tile[:, -1])
    edges.append(tile[10::-1, 0])
    edges.append(tile[10::-1, -1])

    tileEdges[num] = edges

allEdges = [values for edges in tileEdges.values() for values in edges]

# print(allEdges)
matches = {}
for tile, edges in tileEdges.items():
    match = []
    for tile2, edges2 in tileEdges.items():
        if tile == tile2:
            continue

        for edge in edges:
            for edge2 in edges2:
                if (edge == edge2).all():
                    match.append(tile2)

    print(tile)
    matches[tile] = list(set(match))


print(matches)

cornerPieces = [tile for tile, match in matches.items() if len(match) == 2]

print(cornerPieces)


# for edge in list(tileEdges.values())

# for each tile, get its 8 different possible sides (e.g. left right top bottom and each flipped)
# match them up
# find a tile that only has two matches
# make that the top left one
# i need to make sure that if i flip one edge to get things to line up, then i must flip that edge for that shape in general. I think i probably won't have to worry about this.

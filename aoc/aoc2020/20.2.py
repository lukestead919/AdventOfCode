import numpy as np
from numpy.lib.function_base import flip
np.set_printoptions(threshold=np.inf)

with open("DataFiles/20.txt") as f:
    tiles = f.read().replace("#", "1").replace(".", "0").split("\n\n")
    # print(tiles[0])

tilesDict = {}
tileEdges = {}
for tile in tiles:
    tile = tile.splitlines()
    num = int(tile[0][5:-1])
    tile = np.array([[int(c) for c in line] for line in tile[1:]])
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

    matches[tile] = list(set(match))


def flipTile(arr):
    return np.flip(arr, axis=0)


def rotateTile(arr):
    return np.rot90(arr)


def removeEdgesFromTile(arr):
    return arr[1:-1, 1:-1]


def tileMatches(tile, left, top, right, bottom):
    if left is not None and not np.array_equal(tile[:, 0], left):
        return False

    if top is not None and not np.array_equal(tile[0, :], top):
        return False

    if right is not None and not np.array_equal(tile[:, -1], right):
        return False

    if bottom is not None and not np.array_equal(tile[-1, :], bottom):
        return False

    return True


def rotateTileUntilMatches(tile, left, top, right, bottom):
    for i in range(4):
        if (tileMatches(tile, left, top, right, bottom)):
            return tile
        tile = rotateTile(tile)

    tile = flipTile(tile)
    for i in range(4):
        if (tileMatches(tile, left, top, right, bottom)):
            return tile
        tile = rotateTile(tile)

    print("Error!")
    return tile


def addTile(i, j, num, tile):
    global image, imageWithBorders
    tileMap[i, j] = num
    imageWithBorders[10*i:10*(i+1), 10*j:10*(j+1)] = tile
    image[8*i:8*(i+1), 8*j:8*(j+1)] = removeEdgesFromTile(tile)

# for edge in list(tileEdges.values())

# for each tile, get its 8 different possible sides (e.g. left right top bottom and each flipped)
# match them up
# find a tile that only has two matches
# make that the top left one
# i need to make sure that if i flip one edge to get things to line up, then i must flip that edge for that shape in general. I think i probably won't have to worry about this.


cornerPieces = [tile for tile, match in matches.items() if len(match) == 2]

tileMap = np.zeros((12, 12))
imageWithBorders = np.zeros((12*10, 12*10))
image = np.zeros((12*8, 12*8))

topLeftTileNum = cornerPieces[0]
joiningPieces = matches[topLeftTileNum]
topLeftEdges = tileEdges[topLeftTileNum]
rightEdges = tileEdges[joiningPieces[0]]
belowEdges = tileEdges[joiningPieces[1]]
matchingEdgeOnRight = [edge for edge in topLeftEdges if any(
    np.all(edge == edge2) for edge2 in rightEdges)][0]
matchingEdgeBelow = [edge for edge in topLeftEdges if any(
    np.all(edge == edge2) for edge2 in belowEdges)][0]

# need to flip one of these edges so they correctly align with, i could code this but meh
matchingEdgeBelow = flip(matchingEdgeBelow)

tile = tilesDict[topLeftTileNum]

tile = rotateTileUntilMatches(
    tile, None, None, matchingEdgeOnRight, matchingEdgeBelow)

addTile(0, 0, topLeftTileNum, tile)

for i in range(12):
    for j in range(12):
        if i + j == 0:
            continue

        adjacentTiles = 4
        if i == 0 or i == 11:
            adjacentTiles -= 1
        if j == 0 or j == 11:
            adjacentTiles -= 1

        leftTile, topTile, leftEdge, topEdge = None, None, None, None

        availableTiles = [a for a in tilesDict.keys(
        ) if a not in tileMap and len(matches[a]) == adjacentTiles]

        if j > 0:
            leftTile = tileMap[i, j-1]
            leftEdge = imageWithBorders[10*i:10*(i+1), 10*j-1]
            availableTiles = [
                a for a in availableTiles if any(np.all(leftEdge == e) for e in tileEdges[a])]

        if i > 0:
            topTile = tileMap[i-1, j]
            topEdge = imageWithBorders[10*i-1, 10*j:10*(j+1)]
            availableTiles = [
                a for a in availableTiles if any(np.all(topEdge == e) for e in tileEdges[a])]

        if not len(availableTiles) == 1:
            # think i should expect this on the first time
            print("had multiple available tiles")
            print(availableTiles)
        num = availableTiles[0]
        tile = tilesDict[num]

        tile = rotateTileUntilMatches(tile, leftEdge, topEdge, None, None)
        addTile(i, j, num, tile)

print(tileMap)
print(imageWithBorders)
print(image)


seaMonsterLocations = [[0, 0], [1, 1], [1, 4], [0, 5], [0, 6], [1, 7], [1, 10], [0, 11], [0, 12], [1, 13], [1, 16], [0, 17], [0, 18], [-1, 18], [0, 19]]
def seaMonsterAtLocation(image, i, j):
    for loc in seaMonsterLocations:
        iLoc = i + loc[0]
        jLoc = j + loc[1]
        if iLoc < 0 or jLoc < 0 or iLoc >= len(image) or jLoc >= len(image):
            return False
        if image[iLoc, jLoc] == 0:
            return False
    return True

print("Number of 1s =", np.sum(image))

def getNumberOfSeaMonstersInImage(image):
    numOfSeaMonsters = 0
    for i in range(len(image)):
        for j in range(len(image)):
            if seaMonsterAtLocation(image, i, j):
                numOfSeaMonsters += 1

    print(numOfSeaMonsters*len(seaMonsterLocations))

    if numOfSeaMonsters > 0:
        print("Answer =", np.sum(image) - numOfSeaMonsters*len(seaMonsterLocations))


for i in range(4):
    getNumberOfSeaMonstersInImage(image)
    image = rotateTile(image)

image = flipTile(image)
for i in range(4):
    getNumberOfSeaMonstersInImage(image)
    image = rotateTile(image)

def get_closest_cross_to_origin(path1, path2):
    path1Squares = set(get_squares_traversed_by_path(path1))
    path2Squares = set(get_squares_traversed_by_path(path2))



    commonSquares = [square for square in path1Squares if square in path2Squares]
    distances = [abs(s[0]) + abs(s[1]) for s in commonSquares]
    return min(distances)


def get_earliest_cross(path1, path2):
    path1Squares = get_squares_traversed_by_path(path1)
    path2Squares = get_squares_traversed_by_path(path2)

    path1SquaresSet = set(path1Squares)
    path2SquaresSet = set(path2Squares)

    commonSquares = [
        square for square in path1SquaresSet if square in path2SquaresSet]
    distances = [path1Squares.index(s) + path2Squares.index(s) + 2 for s in commonSquares]
    return min(distances)

def get_squares_traversed_by_path(path):
    allSquares = [0]*1000000
    currentSquare = (0,0)
    index = 0
    for line in path:
        direction = line[0]
        length = int(line[1:])
        iStep, jStep = 0, 0
        if direction == "U":
            jStep = 1
        elif direction == "R":
            iStep = 1
        elif direction == "D":
            jStep = -1
        elif direction == "L":
            iStep = -1

        for l in range(length):
            currentSquare = (currentSquare[0] + iStep, currentSquare[1] + jStep)
            allSquares[index] = currentSquare
            index += 1

    return [s for s in allSquares if not s == 0 ]

with open("DataFiles/3.txt") as f:
    input = f.read()

input = [i.split(",") for i in input.splitlines()]
print("Part 1:", get_closest_cross_to_origin(input[0], input[1]))
print("Part 2:", get_earliest_cross(input[0], input[1]))
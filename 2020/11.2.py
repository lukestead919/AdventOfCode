import sys


with open("DataFiles/11.txt") as f:
    seats = f.read().splitlines()
    seats = [[char for char in line] for line in seats]


def isFirstSeatInDirectionOccupied(seats, i, j, iStep, jStep):
    while True:
        i += iStep
        j += jStep
        if (i < 0 or j < 0 or i >= len(seats) or j >= len(seats)):
            return False
        seat = seats[i][j]
        if seat == "#":
            return True
        elif seat == "L":
            return False


def applyCycle(seats):
    newSeats = [list(lst) for lst in seats]

    for i in range(len(seats)):
        row = seats[i]
        for j in range(len(row)):
            seat = row[j]

            if seat == ".":
                newSeats[i][j] = "."
                continue

            adjOccSeats = 0
            if isFirstSeatInDirectionOccupied(seats, i, j, 1, 1):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, 1, 0):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, 1, -1):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, 0, 1):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, 0, -1):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, -1, 1):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, -1, 0):
                adjOccSeats += 1
            if isFirstSeatInDirectionOccupied(seats, i, j, -1, -1):
                adjOccSeats += 1

            if seat == "L" and adjOccSeats == 0:
                newSeats[i][j] = "#"
            elif seat == "#" and adjOccSeats >= 5:
                newSeats[i][j] = "L"
            else:
                newSeats[i][j] = seat

    return newSeats


while True:
    newSeats = applyCycle(seats)
    if newSeats == seats:
        print([item for sublist in seats for item in sublist].count("#"))
        sys.exit()
    seats = newSeats

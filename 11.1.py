import sys


with open("DataFiles/11.txt") as f:
    seats = f.read().splitlines()
    print(seats[0].split(sep=None))
    seats = [[char for char in line] for line in seats]
    # seats = [line.split(sep=None) for line in seats]


def isSeatOccupied(seats, i, j):
    if (i<0 or j<0 or i>=len(seats) or j>=len(seats)):
        return False
    return seats[i][j] == "#"


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
            if isSeatOccupied(seats, i+1, j):
                adjOccSeats += 1
            if isSeatOccupied(seats, i+1, j+1):
                adjOccSeats += 1
            if isSeatOccupied(seats, i+1, j-1):
                adjOccSeats += 1
            if isSeatOccupied(seats, i, j+1):
                adjOccSeats += 1
            if isSeatOccupied(seats, i, j-1):
                adjOccSeats += 1
            if isSeatOccupied(seats, i-1, j):
                adjOccSeats += 1
            if isSeatOccupied(seats, i-1, j-1):
                adjOccSeats += 1
            if isSeatOccupied(seats, i-1, j+1):
                adjOccSeats += 1

            if seat == "L" and adjOccSeats == 0:
                newSeats[i][j] = "#"
            elif seat == "#" and adjOccSeats >= 4:
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

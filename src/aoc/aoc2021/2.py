from utils import read_data_file_as_lines, Point
from functools import reduce


def travel_a(pos: Point, instruction: str) -> Point:
    (direction, distance) = instruction.split(" ")
    distance = int(distance)

    if direction == "forward":
        return Point(pos.x + distance, pos.y)
    elif direction == "down":
        return Point(pos.x, pos.y + distance)
    elif direction == "up":
        return Point(pos.x, pos.y - distance)


def pilot_a(data: list):
    pos = Point(0, 0)
    pos = reduce(travel_a, data, pos)
    return pos.x * pos.y


def travel_b(pos: Point, aim: int, instruction: str) -> (Point, int):
    (direction, distance) = instruction.split(" ")
    distance = int(distance)

    if direction == "forward":
        return Point(pos.x + distance, pos.y + distance * aim), aim
    elif direction == "down":
        return pos, aim + distance
    elif direction == "up":
        return pos, aim - distance


def pilot_b(data: list):
    pos = Point(0, 0)
    aim = 0
    for instruction in data:
        pos, aim = travel_b(pos, aim, instruction)
    return pos.x * pos.y


data = read_data_file_as_lines(2)
print("part 1", pilot_a(data))
print("part 2", pilot_b(data))

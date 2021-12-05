from utils import read_data_file_as_lines, Point
from collections import Counter

data = read_data_file_as_lines(5)


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_points(self) -> list[Point]:
        vector = Point(self.end.x - self.start.x, self.end.y - self.start.y)
        magnitude = max(abs(vector.x), abs(vector.y))  # not really for diagonals but good enough
        angle = Point(vector.x // magnitude, vector.y // magnitude)
        return [self.start + m * angle for m in range(magnitude + 1)]

    def is_diagonal(self) -> bool:
        return self.start.x != self.end.x and self.start.y != self.end.y


class GridCounter:
    def __init__(self):
        self.counter = Counter()

    def add_line(self, line: Line):
        self.counter.update(line.get_points())

    def count_crossings(self):
        return len([v for v in self.counter.values() if v > 1])

    def print(self, length: int):
        for j in range(length):
            print(' '.join([str(self.counter[Point(i, j)]) for i in range(length)]).replace("0", "."))


def parse_line(line: str) -> Line:
    points = line.split(" -> ")
    return Line(parse_point(points[0]), parse_point(points[1]))


def parse_point(point: str) -> Point:
    coords = point.split(",")
    return Point(int(coords[0]), int(coords[1]))


def count_crossings_in_lines(lines: list[Line]) -> int:
    grid_counter = GridCounter()
    for line in lines:
        grid_counter.add_line(line)
    return grid_counter.count_crossings()


lines = [parse_line(line) for line in data]
non_diagonals = [l for l in lines if not l.is_diagonal()]
print("part 1", count_crossings_in_lines(non_diagonals))
print("part 2", count_crossings_in_lines(lines))

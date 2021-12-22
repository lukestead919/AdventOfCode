from utils import read_data_file_as_lines, flatten, not_none
from collections import namedtuple
from dataclasses import dataclass


class Point3D(namedtuple('Point3D', ['x', 'y', 'z'])):
    pass


@dataclass()
class Cuboid:
    low: Point3D
    high: Point3D

    def __repr__(self):
        return f"(low: {self.low}, high: {self.high})"

    def overlaps(self, cuboid):
        return self.overlapping_cuboid(cuboid) is not None

    def overlapping_cuboid(self, cuboid):
        xl = max(self.low.x, cuboid.low.x)
        xh = min(self.high.x, cuboid.high.x)
        yl = max(self.low.y, cuboid.low.y)
        yh = min(self.high.y, cuboid.high.y)
        zl = max(self.low.z, cuboid.low.z)
        zh = min(self.high.z, cuboid.high.z)
        if (xl <= xh) and (yl <= yh) and (zl <= zh):
            return Cuboid(Point3D(xl, yl, zl), Point3D(xh, yh, zh))

    def no_of_points(self):
        return (self.high.x - self.low.x + 1) * (self.high.y - self.low.y + 1) * (self.high.z - self.low.z + 1)

    def fully_contains(self, other):
        return self.overlapping_cuboid(other) == other


class Reactor:
    def __init__(self):
        self.positive_cuboids = []
        self.negative_cuboids = []

    def apply_instruction(self, instruction: str):
        on, cuboid = parse_instruction(instruction)

        # remove any cuboids fully contained in this cuboid. This is purely a performance improvement
        positive_cuboids = [a for a in self.positive_cuboids if not cuboid.fully_contains(a)]
        negative_cuboids = [a for a in self.negative_cuboids if not cuboid.fully_contains(a)]

        # add cuboids to reverse any overlaps. This resets everywhere in the cuboid to 0
        positive_overlaps = not_none([cuboid.overlapping_cuboid(c) for c in positive_cuboids])
        negative_overlaps = not_none([cuboid.overlapping_cuboid(c) for c in negative_cuboids])
        negative_cuboids.extend(positive_overlaps)
        positive_cuboids.extend(negative_overlaps)

        if on:
            positive_cuboids.append(cuboid)

        self.positive_cuboids = positive_cuboids
        self.negative_cuboids = negative_cuboids

    def get_on_in_cuboid(self, cuboid: Cuboid):
        pos = not_none([cuboid.overlapping_cuboid(c) for c in self.positive_cuboids])
        neg = not_none([cuboid.overlapping_cuboid(c) for c in self.negative_cuboids])
        return sum(c.no_of_points() for c in pos) - \
               sum(c.no_of_points() for c in neg)

    def get_total_on(self):
        return sum(c.no_of_points() for c in self.positive_cuboids) - \
               sum(c.no_of_points() for c in self.negative_cuboids)


def parse_instruction(data: str):
    on, cuboid = data.split(" ")
    on = on == "on"
    cuboid = [a[2:].split("..") for a in cuboid.split(",")]
    xl, xh, yl, yh, zl, zh = [int(a) for a in flatten(cuboid)]
    return on, Cuboid(Point3D(xl, yl, zl), Point3D(xh, yh, zh))


def main():
    data = read_data_file_as_lines(22)
    reactor = Reactor()
    for instruction in data:
        reactor.apply_instruction(instruction)

    print("part 1", reactor.get_on_in_cuboid(Cuboid(Point3D(-50, -50, -50), Point3D(50, 50, 50))))
    print("part 2", reactor.get_total_on())


main()

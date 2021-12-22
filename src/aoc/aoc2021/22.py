from utils import read_data_file_as_lines, flatten
import numpy as np
from collections import namedtuple
from dataclasses import dataclass


class Reactor:
    def __init__(self):
        self.cubes = np.zeros((200000, 200000, 200000), dtype=bool)

    def apply_instruction(self, instruction: str):
        on, cuboid = instruction.split(" ")
        on = 1 if on == "on" else 0
        cuboid = [a[2:].split("..") for a in cuboid.split(",")]
        self.apply_cuboid(cuboid, on)

    def apply_cuboid(self, cuboid, on: int):
        xl, xh, yl, yh, zl, zh = [int(a)+125000 for a in flatten(cuboid)]
        self.cubes[xl:xh+1, yl:yh+1, zl:zh+1] = on


class Point3D(namedtuple('Point3D', ['x', 'y', 'z'])):
    pass


@dataclass()
class Cuboid:
    low: Point3D
    high: Point3D

    def __repr__(self):
        return f"(low: {self.low}, high: {self.high})"

    def overlaps(self, cuboid):
        overlap = self.overlapping_cuboid(cuboid)
        return overlap.low.x <= overlap.high.x and \
               overlap.low.y <= overlap.high.y and \
               overlap.low.z <= overlap.high.z

    def overlapping_cuboid(self, cuboid):
        xl = max(self.low.x, cuboid.low.x)
        xh = min(self.high.x, cuboid.high.x)
        yl = max(self.low.y, cuboid.low.y)
        yh = min(self.high.y, cuboid.high.y)
        zl = max(self.low.z, cuboid.low.z)
        zh = min(self.high.z, cuboid.high.z)
        return Cuboid(Point3D(xl, yl, zl), Point3D(xh, yh, zh))

    def no_of_overlaps(self, cuboid):
        return self.overlapping_cuboid(cuboid).no_of_points()

    def no_of_points(self):
        return (self.high.x - self.low.x + 1) * (self.high.y - self.low.y + 1) * (self.high.z - self.low.z + 1)

    def fully_contains(self, other):
        return self.low.x <= other.low.x and self.low.y <= other.low.y and self.low.z <= other.low.z and \
               self.high.x >= other.high.x and self.high.y >= other.high.y and self.high.z >= other.high.z


def parse_instruction(data: str):
    on, cuboid = data.split(" ")
    on = 1 if on == "on" else 0
    cuboid = [a[2:].split("..") for a in cuboid.split(",")]
    xl, xh, yl, yh, zl, zh = [int(a) for a in flatten(cuboid)]
    return on, Cuboid(Point3D(xl, yl, zl), Point3D(xh, yh, zh))


def main():
    data = read_data_file_as_lines(22)
    instructions = [parse_instruction(d) for d in data]
    positive_cuboids = []
    negative_cuboids = []
    print(1)
    # for i, instruction in enumerate(instructions[:10]):
    for i, instruction in enumerate(instructions):
        on, cuboid = instruction

        positive_cuboids = [a for a in positive_cuboids if not cuboid.fully_contains(a)]
        negative_cuboids = [a for a in negative_cuboids if not cuboid.fully_contains(a)]

        positive_overlaps = [cuboid.overlapping_cuboid(c) for c in positive_cuboids if cuboid.overlaps(c)]
        negative_overlaps = [cuboid.overlapping_cuboid(c) for c in negative_cuboids if cuboid.overlaps(c)]
        # print(cuboid)
        # print("positive", positive_overlaps)
        # print("negative", negative_overlaps)
        # print(len(negative_cuboids))
        # print(len(positive_cuboids))
        negative_cuboids.extend(positive_overlaps)
        positive_cuboids.extend(negative_overlaps)
        if on:
            positive_cuboids.append(cuboid)

        # positive_cuboids, negative_cuboids = eliminate_duplicates(positive_cuboids, negative_cuboids)
        # else:
            # negative_cuboids.append(cuboid)
        # print(positive_cuboids, negative_cuboids)
        print(i, len(instructions))

    print(sum(c.no_of_points() for c in positive_cuboids) - sum(c.no_of_points() for c in negative_cuboids))

    # print(on_cuboids[0])
    #
    # print(sum(c.no_of_points() for c in on_cuboids))


def test():
    pass

main()

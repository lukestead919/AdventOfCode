from utils import read_data_file_as_lines, sgn
from dataclasses import dataclass
import random
from collections import Counter
from itertools import product, permutations
from functools import cached_property


class PermsGenerator:
    def __call__(self, *args, **kwargs):
        return self.perms

    @cached_property
    def perms(self):
        perms = set()
        coords = Coords(1, 2, 3)
        while len(perms) < 24:
            perms.add(coords)
            rand = random.randint(0, 1)
            if rand == 0:
                coords = coords.face_up()
            else:
                coords = coords.rotate()

        return [self.create_perm(c) for c in perms]

    def create_perm(self, coords):
        return lambda c: Coords(
                sgn(coords.x)*c.tuple()[abs(coords.x) - 1],
                sgn(coords.y)*c.tuple()[abs(coords.y) - 1],
                sgn(coords.z)*c.tuple()[abs(coords.z) - 1],
            )


perms_generator = PermsGenerator()


@dataclass(unsafe_hash=True)
class Coords:
    x: int
    y: int
    z: int

    def __lt__(self, other):
        return self.tuple() < other.tuple()

    def __add__(self, other):
        return Coords(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return self + Coords(-other.x, -other.y, -other.z)

    def tuple(self):
        return self.x, self.y, self.z

    def face_up(self):  # rotate self up so we're now facing up
        return Coords(self.z, self.y, -self.x)

    def rotate(self):  # keep looking forward but rotate clockwise
        return Coords(self.x, self.z, -self.y)

    def perms(self):
        return [perm(self) for perm in perms_generator.perms]

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Scanner:
    def __init__(self, beacons: set[Coords]):
        self.beacons = beacons
        self.location = None

    def add_beacons(self, beacons: list[Coords]):
        self.beacons.update(beacons)

    def distance_to(self, scanner):
        return (scanner.location - self.location).manhattan_distance()

    def merge_with(self, other):
        other_beacons = other.beacons
        for perm in perms_generator():
            rotated = [perm(beacon) for beacon in other_beacons]
            scanner_position = self.check_for_overlaps(rotated)
            if scanner_position:
                other.location = scanner_position
                translated_beacons = [b - scanner_position for b in rotated]
                self.add_beacons(translated_beacons)

    def check_for_overlaps(self, beacons: list[Coords]):
        differences = [other_beacon - self_beacon for other_beacon, self_beacon in product(beacons, self.beacons)]
        difference_count = Counter(differences).most_common(1)[0]
        if difference_count[1] >= 12:
            scanner_position = difference_count[0]
            return scanner_position


def parse(data: list[str]) -> list[Scanner]:
    data = [a for a in data if not a.startswith("---")]
    curr_beacons = set()
    scanners = []
    for line in data:
        if line == '':
            scanners.append(Scanner(curr_beacons))
            curr_beacons = set()
        else:
            coords = [int(i) for i in line.split(",")]
            curr_beacons.add(Coords(*coords))

    scanners.append(Scanner(curr_beacons))
    return scanners


def test():
    coords = Coords(1, 2, 3)
    perms = coords.perms()
    print(len(perms), perms)


def main():
    data = read_data_file_as_lines(19)
    scanners = parse(data)
    first_scanner = scanners[0]
    first_scanner.location = Coords(0, 0, 0)
    scanners_left = scanners
    while len(scanners_left) > 0:
        for scanner in scanners_left:
            first_scanner.merge_with(scanner)

        scanners_left = [s for s in scanners_left if s.location is None]
        print(len(first_scanner.beacons))

    print("part 1", len(first_scanner.beacons))
    print("part 2", max(a.distance_to(b) for a, b in permutations(scanners, 2)))


# test()
main()

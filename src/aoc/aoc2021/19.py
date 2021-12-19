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
                coords = coords.rotate()
            else:
                coords = coords.flip()

        return [self.create_lambda(c) for c in perms]

    def create_lambda(self, coords):
        return lambda c: Coords(
                sgn(coords.x)*c.tuple()[abs(coords.x) - 1],
                sgn(coords.y)*c.tuple()[abs(coords.y) - 1],
                sgn(coords.z)*c.tuple()[abs(coords.z) - 1],
            )


# class NpPermsGenerator:
#     @cached_property
#     def perms(self):
#         perms = []
#         curr_perm = np.identity(3)
#         while len(perms) < 24:
#             # print(len(perms), perms)
#             if not any(np.array_equal(curr_perm, perm) for perm in perms):
#                 perms.append(curr_perm)
#
#             rand = random.randint(0, 1)
#             if rand == 0:
#                 curr_perm = self.flip(curr_perm)
#             else:
#                 curr_perm = self.rotate(curr_perm)
#
#         return perms
#
#     def flip(self, coords):
#         return np.matmul(np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]), coords)
#
#     def rotate(self, coords):
#         return np.matmul(np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]), coords)


# def matrix_in_list(mat: np.ndarray, mats: list[np.ndarray]):
#     return any(np.array_equal(mat, mat2) for mat2 in mats)

# np_perms_generator = NpPermsGenerator()
# print(np_perms_generator.perms)
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

    def rotate(self):
        return Coords(self.z, self.y, -self.x)

    def flip(self):
        return Coords(self.x, self.z, -self.y)

    def perms(self):
        return [perm(self) for perm in perms_generator.perms]

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


# class Beacon:
#     def __init__(self, coords: Coords):
#         self.coords = coords
#         # self.x = coords[0]
#         # self.y = coords[1]
#         # self.z = coords[2]
#
#     # def array(self):
#     #     return self.coords.coords


class Scanner:
    def __init__(self, beacons: set[Coords]):
        self.beacons = beacons
        self.coords = None

    def add_beacons(self, beacons: list[Coords]):
        self.beacons.update(beacons)

    def distance(self, scanner):
        return (scanner.coords - self.coords).manhattan_distance()

    # def beacon_coords(self):
    #     return [beacon.coords for beacon in self.beacons]

    def overlaps(self, other):
        other_beacons = other.beacons
        for perm in perms_generator():
            rotated = [perm(beacon) for beacon in other_beacons]
            overlap = self.check_for_overlaps(rotated)
            if overlap:
                other.coords = overlap
                translated_beacons = [b - overlap for b in rotated]
                self.add_beacons(translated_beacons)
                return overlap

    def check_for_overlaps(self, beacons: list[Coords]):
        # for other_beacon in beacons:
        #     for self_beacon in self.beacons:
        #         difference = other_beacon - self_beacon
        #         mapped = [other_beacon - difference for other_beacon in beacons]
        #         beacon_arrays = self.beacons
        #         if sum(m in beacon_arrays for m in mapped) >= 12:
        #             return mapped
        differences = [other_beacon - self_beacon for other_beacon, self_beacon in product(beacons, self.beacons)]
        difference_count = Counter(differences).most_common(1)[0]
        # print(difference_count)
        if difference_count[1] >= 12:
            scanner_position = difference_count[0]
            # print("scanner pos", translation)

            return scanner_position
                # difference = other_beacon - self_beacon
                # mapped = [other_beacon - difference for other_beacon in beacons]
                # beacon_arrays = self.beacons
                # if sum(m in beacon_arrays for m in mapped) >= 12:
                #     return mapped


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
    # print(len(perms), perms)


def main():
    data = read_data_file_as_lines(19)
    scanners = parse(data)
    first_scanner = scanners[0]
    first_scanner.coords = Coords(0, 0, 0)
    for i in range(4):

        for scanner in scanners[1:]:
            overlaps = first_scanner.overlaps(scanner)
            # print(overlaps)

        print(len(first_scanner.beacons))
    print(len(first_scanner.beacons))
    print(sorted(first_scanner.beacons))

    print("part 2", max(a.distance(b) for a, b in permutations(scanners, 2)))


# test()
main()

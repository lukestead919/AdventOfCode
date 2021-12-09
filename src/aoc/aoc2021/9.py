from utils import read_data_file_as_lines, Point
import numpy as np
from collections import Counter
import colorsys


class colors: # You may need to change color settings
    BLACK = "000000"
    A = "1E90FF"
    B = "187DE9"
    C = "126AD2"
    D = "0C56BC"
    E = "0643A5"
    F = "00308F"


def getcolour(size: int):
    if size > 5/6:
        return colors.F
    elif size > 4/6:
        return colors.E
    elif size > 3/6:
        return colors.D
    elif size > 2/6:
        return colors.C
    elif size > 1/6:
        return colors.B
    elif size > 0:
        return colors.A
    else:
        return colors.BLACK


def square(hex_string: str) -> str:
    red = int(hex_string[:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)
    return f"\033[48:2::{red}:{green}:{blue}m   \033[49m"


class Heightmap:
    def __init__(self, array: np.ndarray):
        self.array = array
        self.basinmap = np.zeros_like(array)

    def get_neighbours(self, index: Point) -> list[Point]:
        (m, n) = self.array.shape
        return [p for p in index.get_neighbours() if 0 <= p.x < m and 0 <= p.y < n]

    def get_neighbours_values(self, index: Point) -> list[Point]:
        return [self.array[p()] for p in self.get_neighbours(index)]

    def count_minima(self):
        sum = 0
        for i, j in np.ndindex(self.array.shape):
            index = Point(i, j)
            value = self.array[index()]
            neighbours = self.get_neighbours_values(index)
            if all(neighbour > value for neighbour in neighbours):
                sum += value + 1

        return sum

    def populate_basin_map(self):
        for i, j in np.ndindex(self.basinmap.shape):
            self.populate_basin(Point(i, j))

    def populate_basin(self, index: Point):
        if self.array[index()] != 9 and self.basinmap[index()] == 0:
            new_basin = self.basinmap.max() + 1
            self.set_basin(new_basin, index)

    def set_basin(self, basin: int, index: Point):
        if self.array[index()] == 9:
            return
        if self.basinmap[index()] > 0:
            return

        self.basinmap[index()] = basin
        for neighbour in self.get_neighbours(index):
            self.set_basin(basin, neighbour)

    def calculate_basin_score(self):
        counter = Counter(self.basinmap.flatten())
        counter[0] = 0
        most_common = counter.most_common(3)
        most_common_sizes = [b[1] for b in most_common]
        return np.product(most_common_sizes)

    def print(self):
        sizes = Counter(self.basinmap.flatten())
        sizes[0] = 0
        largest = sizes.most_common(1)[0][1]

        def colour(basin_num: int):
            ratio = sizes[basin_num]/largest
            return square(getcolour(ratio))

        colour_map = np.vectorize(colour)(self.basinmap)
        for i in colour_map:
            print(''.join(i))


data = read_data_file_as_lines(9)
datai = [[int(a) for a in line] for line in data]

heightmap = Heightmap(np.array(datai))
heightmap.populate_basin_map()
print("part 1", heightmap.count_minima())
print("part 2", heightmap.calculate_basin_score())

heightmap.print()
from utils import read_data_file_as_lines, Point
import numpy as np
from collections import Counter


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
            if all([neighbour > value for neighbour in neighbours]):
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


data = read_data_file_as_lines(9)
datai = [[int(a) for a in line] for line in data]

heightmap = Heightmap(np.array(datai))
heightmap.populate_basin_map()
print("part 1", heightmap.count_minima())
print("part 2", heightmap.calculate_basin_score())

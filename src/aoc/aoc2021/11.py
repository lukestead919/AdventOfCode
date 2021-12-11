from utils import read_data_file_as_lines, Point
import numpy as np

data = read_data_file_as_lines(11)
data = [[int(v) for v in line] for line in data]
array = np.array(data)

class OctopusGrid:
    def __init__(self, octopi: np.ndarray):
        self.octopi = octopi

    def get_neighbours(self, index: Point):
        m, n = self.octopi.shape
        return [p for p in index.get_all_neighbours() if 0 <= p.x < m and 0 <= p.y < n]

    def generations(self, age) -> int:
        s = 0
        for _ in range(age):
            s += self.generation()
        return s

    def steps_to_sync(self) -> int:
        i = 0
        while True:
            i += 1
            s = self.generation()
            if s == self.octopi.size:
                return i

    def generation(self):
        self.octopi = self.octopi + 1
        to_flash = np.argwhere(self.octopi > 9)
        for o in to_flash:
            self.flash_octopus(Point(o[0], o[1]))

        self.octopi = np.where(self.octopi > 9, 0, self.octopi)

        return len(np.argwhere(self.octopi == 0))

    def flash_octopus(self, index: Point):
        for p in self.get_neighbours(index):
            self.increment_octopus(p)

    def increment_octopus(self, index: Point):
        current = self.octopi[index()]
        self.octopi[index()] += 1
        if current == 9:
            self.flash_octopus(index)


print("part 1", OctopusGrid(array).generations(100))
print("part 2", OctopusGrid(array).steps_to_sync())

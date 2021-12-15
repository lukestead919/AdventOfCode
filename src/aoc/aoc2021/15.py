from utils import read_data_file_as_lines, Point
import numpy as np

large_int = 9999999999


class Pathfinding:
    def __init__(self, grid: np.ndarray):
        self.grid = grid

    def find_minimal_path(self):
        path_grid = np.zeros_like(self.grid) + large_int
        checked_grid = np.zeros_like(self.grid)
        path_grid[-1, -1] = self.grid[-1, -1]
        print(path_grid)
        while path_grid[0, 0] == large_int:
            self.step(path_grid, checked_grid)
        print(path_grid)
        return path_grid[0, 0] - self.grid[0, 0]

    def step(self, path_grid: np.ndarray, checked_grid: np.ndarray):
        potential_next = np.where(np.logical_and(path_grid > 0, checked_grid == 0), path_grid, large_int)
        min_indexes = np.where(potential_next == np.amin(potential_next))
        next_i = list(zip(min_indexes[0], min_indexes[1]))[0]
        # print(potential_next, next_i)
        self.expand(path_grid, checked_grid, Point(next_i[0], next_i[1]))

    def expand(self, path_grid: np.ndarray, checked_grid: np.ndarray, index: Point):
        checked_grid[index()] = 1
        current_path_length = path_grid[index()]
        neighbours = [n for n in index.get_orthogonal_neighbours() if n.in_grid(self.grid)]
        for neighbour in neighbours:
            path_grid[neighbour()] = min(path_grid[neighbour()], current_path_length + self.grid[neighbour()])
        # print(path_grid)


def main():
    data = read_data_file_as_lines(15)
    grid = np.array([[int(a) for a in line] for line in data])
    pathfinder = Pathfinding(grid)
    block = [[np.mod(grid + i+j - 1, 9) + 1 for i in range(5)] for j in range(5)]
    grid_2 = np.block(block)
    pathfinder_2 = Pathfinding(grid_2)
    # print(block)
    print("here", grid_2)
    print("part 1", pathfinder.find_minimal_path())
    print("part 2", pathfinder_2.find_minimal_path())


main()

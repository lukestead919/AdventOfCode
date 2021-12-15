from utils import read_data_file_as_lines, Point
import numpy as np
from time import time
from queue import PriorityQueue

large_int = 9999999999


def heuristic_dijkstras(point: Point):
    return 0


class Pathfinding:
    def __init__(self, grid: np.ndarray, heuristic=heuristic_dijkstras):
        self.grid = grid
        self.risk_grid = np.zeros_like(self.grid) + large_int
        self.queue = PriorityQueue()
        self.checked = set()
        self.heuristic = heuristic

    def find_minimal_path(self):
        start_time = time()
        m, n = self.grid.shape
        end_point = Point(m-1, n-1)

        self.risk_grid[end_point()] = self.grid[end_point()]
        self.add_to_queue(end_point)
        while self.risk_grid[0, 0] == large_int:
            self.step()

        print(f"took {time() - start_time} s to populate distances")
        return self.risk_grid[0, 0] - self.grid[0, 0]

    def step(self):
        next_i = self.queue.get()[1]
        next_point = Point(next_i[0], next_i[1])
        self.expand(next_point)

    def expand(self, index: Point):
        current_path_length = self.risk_grid[index()]
        neighbours = [n for n in index.get_orthogonal_neighbours() if n.in_grid(self.grid)]
        for neighbour in neighbours:
            self.risk_grid[neighbour()] = min(self.risk_grid[neighbour()], current_path_length + self.grid[neighbour()])
            self.add_to_queue(neighbour)

    def add_to_queue(self, index: Point):
        if index not in self.checked:
            self.checked.add(index)
            value = self.risk_grid[index()] + self.heuristic(index)
            self.queue.put((value, index.tuple()))

    def print_path(self):
        start_time = time()
        path = np.zeros_like(self.grid)

        m, n = self.grid.shape
        start_point = Point(0, 0)
        end_point = Point(m-1, n-1)

        current_point = start_point
        while current_point != end_point:
            path[current_point()] = 1
            value_to_look_for = self.risk_grid[current_point()] - self.grid[current_point()]
            for neighbour in [n for n in current_point.get_orthogonal_neighbours() if n.in_grid(path)]:
                if self.risk_grid[neighbour()] == value_to_look_for:
                    current_point = neighbour
                    continue
        path[end_point()] = 1

        with np.printoptions(threshold=np.inf, linewidth=np.inf):
            print(path)
        print(f"took {time() - start_time} s to calculate path")


def main():
    data = read_data_file_as_lines(15)
    grid = np.array([[int(a) for a in line] for line in data])
    pathfinder = Pathfinding(grid)
    print("part 1", pathfinder.find_minimal_path())
    # print(pathfinder.print_path())

    block = [[np.mod(grid + i+j - 1, 9) + 1 for i in range(5)] for j in range(5)]
    grid_2 = np.block(block)
    pathfinder_2 = Pathfinding(grid_2)
    print("part 2", pathfinder_2.find_minimal_path())
    # pathfinder_2.print_path()


def heuristic_manhattan_n(n: int):
    return lambda point: n * (point.x + point.y)


def heuristic_manhattan():
    return heuristic_manhattan_n(1)


def heuristic_testing():
    data = read_data_file_as_lines(15)
    grid = np.array([[int(a) for a in line] for line in data])

    def run_heuristic(heuristic):
        print(heuristic)
        path_length = Pathfinding(grid, heuristic).find_minimal_path()
        print("path length", path_length)
        print()

    run_heuristic(heuristic_dijkstras)
    run_heuristic(heuristic_manhattan_n(1))
    run_heuristic(heuristic_manhattan_n(2))
    run_heuristic(heuristic_manhattan_n(3))
    run_heuristic(heuristic_manhattan_n(4))
    run_heuristic(heuristic_manhattan_n(5))
    run_heuristic(heuristic_manhattan_n(10000))  # basically ignore the value and take the direct path


main()
# heuristic_testing()

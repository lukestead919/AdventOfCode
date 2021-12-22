class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_orthogonal_neighbours(self):
        adjacent = [
            Point(-1, 0),
            Point(1, 0),
            Point(0, -1),
            Point(0, 1),
        ]
        return [self + n for n in adjacent]

    def get_diagonal_neighbours(self):
        adjacent = [
            Point(-1, -1),
            Point(1, -1),
            Point(-1, 1),
            Point(1, 1),
        ]
        return [self + n for n in adjacent]

    def get_all_neighbours(self):
        return self.get_orthogonal_neighbours() + self.get_diagonal_neighbours()

    def in_grid(self, grid):
        m, n = grid.shape
        return 0 <= self.x < m and 0 <= self.y < n

    def tuple(self):
        return self.x, self.y

    def __call__(self, *args, **kwargs):
        return self.tuple()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __rmul__(self, other: int):
        return Point(other * self.x, other * self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def read_file(file_path: str):
    with open(file_path) as f:
        return f.read()


def read_file_as_lines(file_path: str):
    return read_file(file_path).splitlines()


def read_data_file_as_lines(num: int):
    return read_file_as_lines(f"DataFiles/{num}.txt")


def read_data_file_as_ints(num: int):
    return [int(x) for x in read_data_file_as_lines(num)]


def read_data_file_int_list(num: int, delimiter=","):
    return [int(x) for x in read_data_file_as_lines(num)[0].split(delimiter)]


def zip_with_next(lst: list):
    return list(zip(lst, lst[1:]))


def chunked(lst: list, chunk_size: int):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def split_to_ints(str: str) -> list[int]:
    return [int(a) for a in str.strip().split()]


def flatten(lst: list[list]) -> list:
    return [a for b in lst for a in b]


def sgn(a: int) -> int:
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1


def not_none(lst: list) -> list:
    return [a for a in lst if a is not None]

from utils import read_data_file_as_lines, flatten
from collections import Counter

data = read_data_file_as_lines(12)


class Caves:
    def __init__(self, connections):
        cave_dict = {}

        def add_connection(key, value):
            current = cave_dict.get(key)
            current = current if current is not None else []
            current.append(value)
            cave_dict[key] = current

        def connect(a, b):
            add_connection(a, b)
            add_connection(b, a)

        for connection in connections:
            a, b = connection.split('-')
            connect(a, b)

        self.cave_dict = cave_dict

    def paths(self, valid_path) -> list[list]:
        return self.progress_path(['start'], valid_path)

    def progress_path(self, path: list, valid_path) -> list[list]:
        current = path[-1]
        adjacent = self.cave_dict[current]
        possible_paths = [path + [adj] for adj in adjacent]

        valid_paths = [p for p in possible_paths if valid_path(p)]
        complete_paths = [path for path in valid_paths if path[-1] == 'end']

        extended_paths = [self.progress_path(p, valid_path) for p in valid_paths if p not in complete_paths]
        return complete_paths + flatten(extended_paths)


def valid_path_a(path: list[str]):
    counter = Counter(path)
    return not any(k.islower() and v > 1 for k, v in counter.items())


def valid_path_b(path: list[str]):
    counter = Counter(path)
    small_caves_visited = [v for k, v in counter.items() if k.islower() and v > 1]

    if len(small_caves_visited) == 0:
        return True
    elif len(small_caves_visited) == 1 and small_caves_visited[0] == 2 and counter['start'] == 1:
        return True
    else:
        return False


caves = Caves(data)
print("part 1", len(caves.paths(valid_path_a)))
print("part 2", len(caves.paths(valid_path_b)))


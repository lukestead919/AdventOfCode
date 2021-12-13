from utils import read_data_file_as_lines, Point
from functools import reduce


def get_fold(str):
    d, i = str.split('=')
    i = int(i)
    if d == 'x':
        return get_fold_x(i)
    elif d == 'y':
        return get_fold_y(i)


def get_fold_x(x: int):
    return lambda p: Point(x - abs(p.x - x), p.y)


def get_fold_y(y: int):
    return lambda p: Point(p.x, y - abs(p.y - y))


def apply_folds(points: set[Point], folds: list[str]):
    return reduce(lambda points, fold: set(get_fold(fold)(p) for p in points), folds, points)


def print_code(points: set[Point]):
    maxx, maxy = max(p.x for p in points), max(p.y for p in points)
    for j in range(maxy + 1):
        print(' '.join(['#' if Point(i, j) in points else ' ' for i in range(maxx + 1)]))


data = read_data_file_as_lines(13)

divide = data.index("")
points, folds = data[:divide], data[divide+1:]
points = set([Point(int(x), int(y)) for x, y in [p.split(',') for p in points]])
folds = [c for _, _, c in [f.split(" ") for f in folds]]

print("part 1", len(apply_folds(points, folds[:1])))

code = apply_folds(points, folds)
print("part 2")
print_code(code)

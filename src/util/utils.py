# from typing import NewType

# Point = NewType("Point", (int, int))


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def read_file(file_path: str):
    with open(file_path) as f:
        return f.read()


def read_file_as_lines(file_path: str):
    return read_file(file_path).splitlines()


def read_data_file_as_lines(num: int):
    return read_file_as_lines(f"DataFiles/{num}.txt")


def read_data_file_as_ints(num: int):
    return [int(x) for x in read_data_file_as_lines(num)]


def zip_with_next(lst: list):
    return list(zip(lst, lst[1:]))

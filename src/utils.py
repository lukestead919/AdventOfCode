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


def chunked(lst: list, chunk_size: int):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def split_to_ints(str: str) -> list[int]:
    return [int(a) for a in str.strip().split()]



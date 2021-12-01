from src.util.utils import read_data_file_as_ints

data = read_data_file_as_ints(1)


def count_increases(lst: list, offset: int):
    zipped = zip(lst, lst[offset:])
    return sum([1 for x, y in zipped if x < y])


print("part 1", count_increases(data, 1))
print("part 2", count_increases(data, 3))

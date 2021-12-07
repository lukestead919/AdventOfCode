from utils import read_data_file_int_list

data = read_data_file_int_list(7)

median = sorted(data)[len(data)//2]

print("part 1", sum([abs(d - median) for d in data]))


def fuel_burned_for_distance(d: int) -> int:
    return d*(d+1)//2


fuels_for_positions = [sum([fuel_burned_for_distance(abs(d-i)) for d in data]) for i in range(1000)]

print("part 2", min(fuels_for_positions))

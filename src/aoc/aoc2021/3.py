from utils import read_data_file_as_lines

data = read_data_file_as_lines(3)

test = ["00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"]


def merge_binaries(lst: list[str]) -> str:
    bin_length = len(lst[0])
    lst_length = len(lst)
    bitwise = [[int(lst[j][i]) for j in range(lst_length)] for i in range(bin_length)]
    sums = [sum(a) for a in bitwise]
    collapsed = ["1" if a >= lst_length / 2 else "0" for a in sums]
    return ''.join(collapsed)


def calculate_power(data: list[str]):
    binary = merge_binaries(data)
    print(binary)
    binary_flip = flip_binary(binary)
    gamma = int(binary, 2)
    epsilon = int(binary_flip, 2)
    return gamma * epsilon


def flip_binary(bin: str):
    return ''.join([flip_bit(b) for b in bin])


def flip_bit(bit: str) -> str:
    return "1" if bit == "0" else "0"


def find_common(lst: list[str], most_common: bool) -> str:
    matches = lst[::]
    index = 0
    while len(matches) > 1:
        to_match = merge_binaries(matches)[index]
        if not most_common:
            to_match = flip_bit(to_match)
        matches = [a for a in matches if a[index] == to_match]
        index += 1
        if len(matches) == 1:
            return matches[0]


def calculate_life_support(data: list[str]):
    o2 = find_common(data, True)
    co2 = find_common(data, False)
    print(o2, co2)
    return int(o2, 2) * int(co2, 2)


# print("part 1 test", calculate_power(test))
# print("part 2 test", calculate_life_support(test))

print("part 1", calculate_power(data))
print("part 2", calculate_life_support(data))

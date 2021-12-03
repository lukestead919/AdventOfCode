from utils import read_data_file_as_lines

data = read_data_file_as_lines(3)


def merge_binaries(binaries: list[str]) -> str:
    bin_length = len(binaries[0])
    collapsed = [merge_bits_at_index(binaries, i) for i in range(bin_length)]
    return ''.join(collapsed)


def merge_bits_at_index(binaries: list[str], index: int) -> str:
    bits = [binaries[i][index] for i in range(len(binaries))]
    return merge_bits(bits)


def merge_bits(bits: list[str]) -> str:
    num_of_ones = sum(int(b) for b in bits)
    return "1" if num_of_ones >= len(bits) / 2 else "0"


def calculate_power(data: list[str]):
    binary = merge_binaries(data)
    binary_flip = flip_binary(binary)
    gamma = int(binary, 2)
    epsilon = int(binary_flip, 2)
    return gamma * epsilon


def flip_binary(bin: str):
    return ''.join([flip_bit(b) for b in bin])


def flip_bit(bit: str) -> str:
    return str(1-int(bit))


def find_rating(lst: list[str], most_common: bool) -> str:
    matches = lst[::]
    for index in range(len(lst[0])):
        to_match = merge_bits_at_index(matches, index)
        if not most_common:
            to_match = flip_bit(to_match)

        matches = [a for a in matches if a[index] == to_match]
        if len(matches) == 1:
            return matches[0]


def calculate_life_support(data: list[str]):
    o2 = find_rating(data, True)
    co2 = find_rating(data, False)
    print(o2, co2)
    return int(o2, 2) * int(co2, 2)


print("part 1", calculate_power(data))
print("part 2", calculate_life_support(data))

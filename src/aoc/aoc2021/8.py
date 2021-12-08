from utils import read_data_file_as_lines, flatten
from itertools import permutations

data = read_data_file_as_lines(8)


seg_dict = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}


def sort_string(str):
    return ''.join(sorted(str))


class Input:
    def __init__(self, input: list[str]):
        self.input = input

    def test_perm(self, perm: dict):
        translation = "".maketrans(perm)
        mapping = [sort_string(i.translate(translation)) for i in self.input]
        return all([i in seg_dict.keys() for i in mapping])


class Output:
    def __init__(self, output: list):
        self.output = output

    def decipher(self, perm: dict) -> int:
        translation = "".maketrans(perm)
        mapping = [sort_string(i.translate(translation)) for i in self.output]
        nums = [seg_dict[m] for m in mapping]
        return int(''.join([str(i) for i in nums]))


class Combination:
    def __init__(self, input: Input, output: Output):
        self.input = input
        self.output = output

    def get_perms(self):
        seg_values = "abcdefg"
        return [dict(zip(seg_values, p)) for p in permutations(seg_values)]

    def decipher(self):
        for perm in self.get_perms():
            if self.input.test_perm(perm):
                return self.output.decipher(perm)


def parse_line(line: str):
    input, output = line.split(" | ")
    input = Input(input.split(" "))
    output = Output(output.split(" "))
    return Combination(input, output)


lines = [parse_line(line) for line in data]
easy_lengths = [2, 3, 4, 7]
outputs = flatten([line.output.output for line in lines])
print("part 1", len([o for o in outputs if len(o) in easy_lengths]))

deciphered = [line.decipher() for line in lines]
print(deciphered)

print("part 2", sum(deciphered))

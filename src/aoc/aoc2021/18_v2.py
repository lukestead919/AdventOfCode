from utils import read_data_file_as_lines
from functools import reduce
from itertools import product
from dataclasses import dataclass


@dataclass()
class NumberWithDepth:
    value: int
    depth: int

    def increment_depth(self):
        return NumberWithDepth(self.value, self.depth + 1)

    def decrement_depth(self):
        return NumberWithDepth(self.value, self.depth - 1)

    def split(self):
        return [
            NumberWithDepth(self.value // 2, self.depth + 1),
            NumberWithDepth(self.value - (self.value // 2), self.depth + 1)
        ]


@dataclass()
class SnailFishNumber:
    numbers: list[NumberWithDepth]

    def __add__(self, other):
        sfn = SnailFishNumber([n.increment_depth() for n in self.numbers + other.numbers])
        sfn.reduce()
        return sfn

    def reduce(self):
        while True:
            length = len(self.numbers)
            self.explode()
            if length != len(self.numbers):
                continue

            self.split()
            if length != len(self.numbers):
                continue
            break

    def explode(self):
        explode_candidates = [i for i, x in enumerate(self.numbers) if x.depth > 4]
        if len(explode_candidates) > 0:
            index = explode_candidates[0]
            left, right = self.numbers[index:index+2]
            self.numbers = self.numbers[:index] + [NumberWithDepth(0, left.depth - 1)] + self.numbers[index+2:]
            self.add(index - 1, left.value)
            self.add(index + 1, right.value)

    def add(self, index: int, num: int):
        if 0 <= index < len(self.numbers):
            self.numbers[index].value += num

    def split(self):
        split_candidates = [(i, x) for i, x in enumerate(self.numbers) if x.value > 9]
        if len(split_candidates) > 0:
            index, to_split = split_candidates[0]
            self.numbers = self.numbers[:index] + to_split.split() + self.numbers[index+1:]

    def magnitude(self):
        if len(self.numbers) == 1 and self.numbers[0].depth == 0:
            return self.numbers[0].value
        else:
            left, right = self.get_pair()
            return 3 * left.magnitude() + 2 * right.magnitude()

    def get_pair(self) -> tuple:
        halfway = self.halfway()
        numbers = [n.decrement_depth() for n in self.numbers]
        return SnailFishNumber(numbers[:halfway]), \
            SnailFishNumber(numbers[halfway:])

    def halfway(self):
        percentage_complete = [sum(pow(2, -nums.depth) for nums in self.numbers[:i]) for i in range(len(self.numbers))]
        return percentage_complete.index(0.5)


def parse(s: str):
    nums = []
    depth = 0
    for idx, char in enumerate(s):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char.isnumeric():
            nums.append(NumberWithDepth(int(char), depth))

    return SnailFishNumber(nums)


def main():
    data = read_data_file_as_lines(18)
    snailfishNumbers = [parse(s) for s in data]
    result = reduce(lambda x, y: x + y, snailfishNumbers)
    print("part 1", result.magnitude())
    print("part 2", max((x + y).magnitude() for x, y in product(snailfishNumbers, repeat=2)))


main()

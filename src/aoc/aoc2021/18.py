from utils import read_data_file_as_lines
from functools import reduce
from itertools import product
from copy import deepcopy
# from abc import ABC, abstractmethod

data = read_data_file_as_lines(18)


# class Entry:
#     @abstractmethod
#     def add_left(self, num: int):
#
# class Number(Entry):


class Pair:
    def __init__(self, first, second):
        self.first = deepcopy(first)
        self.second = deepcopy(second)

    def __add__(self, other):
        return self.add_and_reduce(other)

    def __str__(self):
        return f"[{self.first},{self.second}]"

    def __repr__(self):
        return self.__str__()

    def add_and_reduce(self, other):
        pair = Pair(self, other)
        pair.reduce()
        return pair

    def magnitude(self):
        if isinstance(self.first, Pair):
            mag_left = self.first.magnitude()
        else:
            mag_left = self.first

        if isinstance(self.second, Pair):
            mag_right = self.second.magnitude()
        else:
            mag_right = self.second

        return 3 * mag_left + 2 * mag_right

    def reduce(self):
        # original = self.deepcopy()
        while True:
            result = self.explode(0)
            if result:
                continue
            # print(self)
            # if original != self:
            #     original = self
            #     continue

            result = self.split()
            if result:
                continue
            # if original != self:
            #     original = self
            #     continue
            break

    def explode(self, depth: int) -> tuple[int, int]:
        if depth == 4:
            return self.first, self.second

        if isinstance(self.first, Pair):
            first_explode = self.first.explode(depth + 1)
            if first_explode is not None:
                if depth == 3:
                    self.first = 0

                if isinstance(self.second, int):
                    self.second += first_explode[1]
                else:
                    self.second.add_left(first_explode[1])

                return first_explode[0], 0

        if isinstance(self.second, Pair):
            second_explode = self.second.explode(depth + 1)
            if second_explode is not None:
                if depth == 3:
                    self.second = 0

                # add_to_left = second_explode
                if isinstance(self.first, int):
                    self.first += second_explode[0]
                else:
                    self.first.add_right(second_explode[0])

                return 0, second_explode[1]

    def add_left(self, num: int):
        if isinstance(self.first, int):
            self.first += num
        else:
            self.first.add_left(num)

    def add_right(self, num: int):
        if isinstance(self.second, int):
            self.second += num
        else:
            self.second.add_right(num)

    def split(self):
        if isinstance(self.first, int) and self.first > 9:
            self.first = Pair(self.first // 2, self.first - (self.first // 2))
            return True
        elif isinstance(self.first, Pair):
            split_result = self.first.split()
            if split_result is not None:
                return split_result

        if isinstance(self.second, int) and self.second > 9:
            self.second = Pair(self.second // 2, self.second - (self.second // 2))
            return True
        elif isinstance(self.second, Pair):
            split_result = self.second.split()
            if split_result is not None:
                return split_result


def parse(s: str):
    if s.startswith("["):
        open_brackets = 0
        middle = s[1:-1]
        for idx, char in enumerate(middle):
            if char == "[":
                open_brackets += 1
            elif char == "]":
                open_brackets -= 1
            elif char == "," and open_brackets == 0:
                first = middle[0:idx]
                second = middle[idx+1:]
                # print(s, first, second)
                return Pair(parse(first), parse(second))
    else:
        return int(s)


def test():
    add = parse("[[[[4,3],4],4],[7,[[8,4],9]]]") + parse("[1,1]")
    print(add)
    add.reduce()
    print(add)


def main():
    pairs = [parse(s) for s in data]
    result = reduce(lambda x, y: x+y, pairs)
    print("part 1", result.magnitude())
    print("part 2", max(x.add_and_reduce(y).magnitude() for x, y in product(pairs, pairs)))


# test()
main()

from utils import read_data_file_as_lines
from functools import reduce
from itertools import product
from copy import deepcopy
from abc import ABC, abstractmethod
from typing import Optional

data = read_data_file_as_lines(18)


class Entry(ABC):
    @abstractmethod
    def add_right(self, num: int) -> None:
        pass

    @abstractmethod
    def add_left(self, num: int) -> None:
        pass

    @abstractmethod
    def magnitude(self) -> int:
        pass

    @abstractmethod
    def explode(self, depth: int) -> Optional[tuple]:
        pass

    @abstractmethod
    def split(self) -> Optional:
        pass


class Regular(Entry):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    def add_right(self, num: int):
        self.value += num

    def add_left(self, num: int):
        self.value += num

    def magnitude(self):
        return self.value

    def explode(self, depth: int):
        pass

    def split(self):
        if self.value > 9:
            return Pair(Regular(self.value // 2), Regular(self.value - (self.value // 2)))


class Pair(Entry):
    def __init__(self, first: Entry, second: Entry):
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
        return 3 * self.first.magnitude() + 2 * self.second.magnitude()

    def reduce(self):
        while True:
            result = self.explode(0)
            if result:
                continue

            result = self.split()
            if result:
                continue
            break

    def explode(self, depth: int) -> tuple[int, int]:
        if depth == 4:
            return self.first.value, self.second.value

        explode_result = self.first.explode(depth + 1)
        if explode_result:
            if depth == 3:
                self.first = Regular(0)
            add_to_left, add_to_right = explode_result

            self.second.add_left(add_to_right)
            return explode_result[0], 0

        explode_result = self.second.explode(depth + 1)
        if explode_result:
            if depth == 3:
                self.second = Regular(0)
            add_to_left, add_to_right = explode_result

            self.first.add_right(add_to_left)
            return 0, explode_result[1]

    def add_left(self, num: int):
        self.first.add_left(num)

    def add_right(self, num: int):
        self.second.add_right(num)

    def split(self):
        split_result = self.first.split()
        if split_result:
            if isinstance(split_result, Entry):
                self.first = split_result
            return True

        split_result = self.second.split()
        if split_result:
            if isinstance(split_result, Entry):
                self.second = split_result
            return True


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
                return Pair(parse(first), parse(second))
    else:
        return Regular(int(s))


def test():
    add = parse("[[[[4,3],4],4],[7,[[8,4],9]]]") + parse("[1,1]")
    print(add)
    add.reduce()
    print(add)


def main():
    pairs = [parse(s) for s in data]
    result = reduce(lambda x, y: x+y, pairs)
    print("part 1", result.magnitude())
    print("part 2", max((x+y).magnitude() for x, y in product(pairs, pairs)))


# test()
main()

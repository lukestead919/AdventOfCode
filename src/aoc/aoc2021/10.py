from utils import read_data_file_as_lines
from functools import reduce

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
openers = pairs.keys()
closers = pairs.values()
compile_error_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_error_values = {')': 1, ']': 2, '}': 3, '>': 4}


def calculate_incomplete_error_score(str):
    return reduce(lambda current, char: 5*current + incomplete_error_values[char], str, 0)


class Line:
    def __init__(self, line):
        self.line = line

    def compile_error_score(self):
        stack = []
        for char in self.line:
            if char in openers:
                stack.append(char)
            elif char in closers:
                open = stack.pop()
                if pairs[open] != char:
                    return compile_error_values[char]
            else:
                return 0

        return 0

    def incomplete_error_score(self):
        stack = []
        for char in self.line:
            if char in openers:
                stack.append(char)
            elif char in closers:
                open = stack.pop()
                if pairs[open] != char:
                    return 0
            else:
                return 0

        to_close = [pairs[open] for open in stack][::-1]

        score = calculate_incomplete_error_score(''.join(to_close))
        return score


def part_b(lines):
    scores = [l.incomplete_error_score() for l in lines]
    scores = [s for s in scores if s > 0]
    return sorted(scores)[(len(scores)-1) // 2]


data = read_data_file_as_lines(10)
lines = [Line(line) for line in data]
print("part 1", sum(l.compile_error_score() for l in lines))
print("part 2", part_b(lines))

from utils import read_data_file_as_lines, chunked
from collections import namedtuple, defaultdict
from math import trunc
from itertools import product
from functools import cache, reduce


class Memory(namedtuple('memory', ['w', 'x', 'y', 'z'], defaults=(0, 0, 0, 0))):
    pass

# def truncate(a, b):


class Block:
    def __init__(self, divides: bool, x_adder: int, y_adder: int):
        self.divides = divides
        self.x_adder = x_adder
        self.y_adder = y_adder
        self.offset_to_pair = 0

    def max_value(self):
        return min(9, 9 - self.offset_to_pair)

    def min_value(self):
        return max(1, 1 - self.offset_to_pair)

    def apply(self, z: int, input: int):
        x = (z % 26) + self.x_adder
        if self.divides:
            z = trunc(z / 26)  # take off end value (base 26)
        if input == x:
            return z
        return 26*z + input + self.y_adder  # add input + y on the end



class ALU:
    def __init__(self, instructions):
        self.instructions = [self.parse_instruction(i) for i in instructions]
        self.instruction_blocks = [self.parse_instruction_block(block) for block in (chunked(instructions, 18))]
        self.memory = defaultdict(int)
        self.input_iterator = None

    def parse_instruction(self, instruction: str):
        fn, *args = instruction.split(" ")
        if fn == 'inp':
            return lambda: self.assign(args[0], next(self.input_iterator))
        else:
            def v(s: str):
                # if s == 'w':
                #     print('w', self.memory)
                return self.memory[s] if s.isalpha() else int(s)
            x, y = args
            if fn == 'add':
                return lambda: self.assign(x, v(x)+v(y))
            elif fn == 'mul':
                return lambda: self.assign(x, v(x)*v(y))
            elif fn == 'div':
                return lambda: self.assign(x, int(v(x) / v(y)))
            elif fn == 'mod':
                return lambda: self.assign(x, v(x) % v(y))
            elif fn == 'eql':
                return lambda: self.assign(x, v(x) == v(y))

    def pair_blocks(self):
        unpaired = []
        paired = []
        for block in self.instruction_blocks:
            if not block.divides:
                unpaired.append(block)
            else:
                paired.append((unpaired.pop(), block))
        assert len(unpaired) == 0
        return paired

    def get_lims(self):
        for first, second in self.pair_blocks():
            offset = first.y_adder - second.x_adder
            print(offset)

    def calculate_pair_offsets(self):
        for left, right in self.pair_blocks():
            offset = left.y_adder + right.x_adder
            if offset > 8:
                offset -= 26
            left.offset_to_pair = offset
            right.offset_to_pair = -offset


    # def parse_instruction_inverse(self, instruction: str):
    #     fn, *args = instruction.split(" ")
    #     if fn == 'inp':
    #         print(self.memory['w'])
    #     else:
    #         def v(s: str):
    #             return self.memory[s] if s.isalpha() else int(s)
    #         x, y = args
    #         if fn == 'add':
    #             return lambda: self.assign(x, v(x)-v(y))
    #         elif fn == 'mul':
    #             return lambda: self.assign(x, v(x)//v(y))
    #         elif fn == 'div':
    #             return lambda: self.assign(x, int(v(x) / v(y)))
    #         elif fn == 'mod':
    #             return lambda: self.assign(x, v(x) % v(y))
    #         elif fn == 'eql':
    #             return lambda: self.assign(x, v(y) if v(x) == 1)

    def assign(self, var: str, val: int):
        # print(var, val)
        self.memory[var] = val

    def compute(self, input):
        assert len(input) == 14
        memory = defaultdict(int)
        self.memory = memory
        self.input_iterator = iter(input)
        for instruction in self.instructions:
            instruction()

        return self.memory

    def fast_compute(self, input):
        assert len(input) == 14
        z = 0
        for i, instruction_block in enumerate(self.instruction_blocks):
            z = instruction_block.apply(z, input[i])

        return z

    def parse_instruction_block(self, block: list[str]):
        assert len(block) == 18
        divisor = int(block[4].split(" ")[-1])
        divides = divisor == 26
        x_adder = int(block[5].split(" ")[-1])
        y_adder = int(block[15].split(" ")[-1])

        return Block(divides, x_adder, y_adder)
        # def fn(z, input) -> int:
        #     x = (z % 26) + x_adder
        #     z = trunc(z / divisor)  # take off end value (base 26)
        #     if input == x:
        #         return z
        #     return 26*z + input + y_adder  # add input + y on the end
        #
        # return fn


def test():
    binary = ['inp w', 'inp w',
    'add z w',
    'mod z 2',
    'div w 2',
    'add y w',
    'mod y 2',
    'div w 2',
    'add x w',
    'mod x 2',
    'div w 2',
    'mod w 2']
    alu = ALU(binary)
    print(alu.compute([9, 7]))

    p = 4.25
    w = 3
    n = -4.25
    all = [p, w, n]
    print([a for a in all])
    print([int(a) for a in all])
    print([trunc(a) for a in all])
    print([a // 1 for a in all])

    alu = ALU(['eql z 0', 'eql x 1', 'add w z', 'add w z', 'mul w w', 'mul w w', 'mul w w', 'mul w -1', 'div w 255', 'add y -12'])
    print(alu.compute([0]))


def unknown(num: int):
    return tuple([range(1, 10) for _ in range(num)])
    # return tuple([range(9, 0, -1) for _ in range(num)])


def main():
    data = read_data_file_as_lines(24)
    alu = ALU(data)

    alu.calculate_pair_offsets()
    print(''.join([str(a.max_value()) for a in alu.instruction_blocks]))
    print(''.join([str(a.min_value()) for a in alu.instruction_blocks]))

    input = 11812117911237
    print(alu.fast_compute([int(a) for a in str(input)]))
    print(alu.fast_compute([3, 7, 9, 2, 9, 8, 8, 9, 9, 1, 3, 9, 9, 9]))
    print(alu.fast_compute([9, 9, 2, 9, 8, 9, 9, 3, 1, 9, 9, 8, 7, 3]))

    # input = 99298999499999
    #
    # input = [int(a) for a in str(input)]
    # result = alu.compute(input)
    # print(result)

    # for i in product(*unknown(14)):
    # # for i in product([9], [9], *unknown(1), [9], *unknown(1), [9], [9], [9],  *unknown(6)):
    #     # print(i)
    #     if i[-1] == i[-2] == i[-3] == i[-4] == i[-5] == 9:
    #         print(i)
    #         print(alu.fast_compute(i))
    #     # result = alu.compute(i)['z']
    #     fast_result = alu.fast_compute(i)
    #     # assert result == fast_result
    #     # print(result)
    #     if fast_result == 0:
    #         print("part 1", i, fast_result)
    #         # break

    # for i in product(*unknown(14)):
    # # for i in product(*unknown(3), [6], *unknown(5), [2], [5], [4], [4], *unknown(1)):
    #     # print(i)
    #     # if i[-1] == i[-2] == i[-3] == i[-4] == i[-5] == 9:
    #     #     print(i)
    #     # print(alu.compute(i))
    #     result = alu.compute(i)
    #     print(result)
    #     if result['z'] == 0:
    #         print("part 1", i)
    #         break


    # input = [9] * 14
    # for i in range(13, -1, -1):
    #     for val in range(9, 0, -1):
    #     if input[i] > 1:
    #         continue
    #     for val in range(1, 10):
    #         input[i] = val
    #         result = alu.compute(input)
    #         print(result)
    #         valid = result['z'] == 0
    #         if not valid:
    #             input[i] -= 1
    #             break

    print("not found")



# test()
main()

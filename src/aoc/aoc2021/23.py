from enum import Enum
from copy import deepcopy


class Letter(Enum):
    A = 1
    B = 10
    C = 100
    D = 1000


class Room:
    def __init__(self, owner: Letter, spaces: list):
        self.owner = owner
        self.spaces = spaces

    def complete(self):
        return all(space == self.owner for space in self.spaces)

    def letters(self):
        return [l for l in self.spaces if l != '.']

    def valid_move_in(self):
        return all(space in ('.', self.owner) for space in self.spaces)

    def valid_move_out(self):
        return not self.valid_move_in() and not all(space == '.' for space in self.spaces)

    def free_spaces(self) -> int:
        return self.spaces.count('.')

    def get_next_free_space_index(self):
        return len(self.spaces) - self.free_spaces()

    def get_top_letter(self):
        return self.spaces[self.get_top_letter_index()]

    def get_top_letter_index(self):
        return self.get_next_free_space_index() - 1

    def distance(self, index: int):
        return len(self.spaces) - index

    def move_in(self, letter: Letter) -> int:
        assert self.valid_move_in()
        assert letter == self.owner
        idx = self.get_next_free_space_index()
        self.spaces[idx] = letter
        return self.distance(idx)

    def move_out(self) -> tuple[Letter, int]:
        idx = self.get_top_letter_index()
        letter = self.spaces[idx]
        self.spaces[idx] = '.'
        return letter, self.distance(idx)


class Board:
    def __init__(self, spaces: list):
        self.spaces = spaces

    def rooms(self):
        return [a for a in self.spaces if isinstance(a, Room)]

    def letter_room(self, letter: Letter):
        return [room for room in self.rooms() if room.owner == letter][0]

    def free_letters(self):
        return [a for a in enumerate(self.spaces) if isinstance(a[1], Letter)]

    def free_spaces(self):
        return [idx for idx, a in enumerate(self.spaces) if a == '.']

    def valid_path(self, idx1: int, idx2: int):
        mi = min(idx1, idx2)
        ma = max(idx1, idx2)
        return len([a for a in self.spaces[mi+1:ma] if isinstance(a, Letter)]) == 0

    # def blockers(self, idx):
    #     letter = self.spaces[idx]
    #     room = self.letter_room(letter)
    #     return [a for idx, a in enumerate(self.spaces)]
    #
    # def valid(self):
    #     blockers.
    #     return True

    def min_points_to_complete(self):
        points = 0
        for idx, letter in self.free_letters():
            room = self.letter_room(letter)
            room_idx = self.room_index(room)
            points += abs(idx - room_idx) * letter.value

        for room in self.rooms():
            room_idx = self.room_index(room)
            letters_need_moving = False
            for idx, letter in enumerate(room.letters()):
                if letter != room.owner:
                    letters_need_moving = True
                if letters_need_moving:
                    distance = room.distance(idx)  # distance to move letters in/out
                    points += distance * room.owner.value  # Count points to move the correct letters in
                    distance += min(2, abs(room_idx - self.letter_room_index(letter)))  # move the letters to the correct room (min 2 moves - if in correct room have to move out of way first)
                    points += distance * letter.value  # Count distance to move incorrect letters to above the correct room

        # print(points)
        return points

    def complete(self):
        return all(room.complete() for room in self.rooms())

    def room_index(self, room: Room):
        return self.spaces.index(room)

    def letter_room_index(self, letter: Letter):
        return self.room_index(self.letter_room(letter))

    def set(self, index, to):
        self.spaces[index] = to


class Game:
    def __init__(self):
        self.min_points = 0

    def play(self, board: Board):
        self.min_points = 999999999
        self.iterate(0, board)
        return self.min_points

    def iterate(self, points_so_far: int, board: Board):
        if (points_so_far + board.min_points_to_complete()) >= self.min_points:
            return

        if board.complete():
            if points_so_far < self.min_points:
                self.min_points = points_so_far
                print(points_so_far)
            return

        self.iterate_all_possible_moves(board, points_so_far)

    def iterate_all_possible_moves(self, board: Board, points: int):
        for idx, letter in board.free_letters():
            room = board.letter_room(letter)
            room_index = board.room_index(room)
            if room.valid_move_in() and board.valid_path(idx, room_index):
                b = deepcopy(board)
                room = b.letter_room(room.owner)
                b.set(idx, '.')
                distance = abs(idx - room_index)
                distance += room.move_in(letter)
                # print("move in ", letter)
                self.iterate(points + distance * letter.value, b)
                return   # moving in straight away is always optimal

        for room in [room for room in board.rooms() if room.valid_move_out()]:
            room_index = board.room_index(room)

            # see if we can move straight in to the good room
            top_letter = room.get_top_letter()
            letter_room, letter_room_index = board.letter_room(top_letter), board.letter_room_index(top_letter)
            if letter_room.valid_move_in() and board.valid_path(room_index, letter_room_index):
                b = deepcopy(board)
                room = b.letter_room(room.owner)
                letter, distance = room.move_out()
                new_room = b.letter_room(letter)
                distance += new_room.move_in(letter)
                distance += abs(b.room_index(new_room) - room_index)
                self.iterate(points + distance * letter.value, b)
                return  # moving in straight away is always optimal

            for idx in sorted(board.free_spaces(), key=lambda x: -abs(x - room_index)):
                if board.valid_path(idx, room_index):
                    b = deepcopy(board)
                    room = b.letter_room(room.owner)
                    letter, distance = room.move_out()
                    distance += abs(idx - room_index)
                    b.set(idx, letter)
                    self.iterate(points + distance * letter.value, b)


def main():
    game = Game()
    a = Room(Letter.A, [Letter.D, Letter.A])
    b = Room(Letter.B, [Letter.A, Letter.C])
    c = Room(Letter.C, [Letter.D, Letter.B])
    d = Room(Letter.D, [Letter.B, Letter.C])
    spaces = ['.', '.', a, '.', b, '.', c, '.', d, '.', '.']
    print("part 1", game.play(Board(spaces)))

    a = Room(Letter.A, [Letter.D, Letter.D, Letter.D, Letter.A])
    b = Room(Letter.B, [Letter.A, Letter.B, Letter.C, Letter.C])
    c = Room(Letter.C, [Letter.D, Letter.A, Letter.B, Letter.B])
    d = Room(Letter.D, [Letter.B, Letter.C, Letter.A, Letter.C])
    spaces2 = ['.', '.', a, '.', b, '.', c, '.', d, '.', '.']
    print("part 2", game.play(Board(spaces2)))


main()

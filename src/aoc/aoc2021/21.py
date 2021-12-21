from utils import read_data_file_as_lines
from functools import cache, reduce
from itertools import product

class Game1:
    def __init__(self, player1: int, player2: int):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.round = 0

    def play(self):
        while self.player1_score < 1000 and self.player2_score < 1000:
            self.play_next()
        # print(self.round, self.player1_score, self.player2_score)
        return self.round * min(self.player1_score, self.player2_score)

    def play_next(self):
        score = sum([self.roll_dice() for _ in range(3)])
        # print(score)
        if self.round % 2 == 1:
            self.player1 = ((self.player1 + score - 1) % 10) + 1
            self.player1_score += self.player1
        else:
            self.player2 = ((self.player2 + score - 1) % 10) + 1
            self.player2_score += self.player2

    def roll_dice(self):
        self.round += 1
        return ((self.round - 1) % 100) + 1


class Scores:
    def __init__(self, player1: int, player2: int):
        self.player1 = player1
        self.player2 = player2

    def __add__(self, other):
        return Scores(self.player1 + other.player1, self.player2 + other.player2)

    def __repr__(self):
        return f"({self.player1}, {self.player2})"


class Game2:
    def __init__(self, player1: int, player2: int):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.round = 0

    @cache
    def play_from_start(self):
        scores = self.play(self.player1, self.player2, 0, 0, True)
        return max(scores.player1, scores.player2)

    @cache
    def play(self, player1: int, player2: int, player1_score: int, player2_score: int, player1_turn: bool) -> Scores:
        print(player1, player2, player1_score, player2_score)
        if player1_score >= 21:
            return Scores(1, 0)
        elif player2_score >= 21:
            return Scores(0, 1)

        scores = [sum(p) for p in product(range(1, 4), repeat=3)]
        if player1_turn:
            new_player1s = [((player1 + score - 1) % 10) + 1 for score in scores]
            s = [self.play(new_player1, player2, player1_score + new_player1, player2_score, False) for new_player1 in
                 new_player1s]
            return reduce(lambda x, y: x+y, s)
        else:
            new_player2s = [((player2 + score - 1) % 10) + 1 for score in scores]
            s = [self.play(player1, new_player2, player1_score, player2_score + new_player2, True) for new_player2 in new_player2s]
            return reduce(lambda x, y: x+y, s)


    # def play(self):
    #     while self.player1_score < 1000 and self.player2_score < 1000:
    #         self.play_next()
    #     return self.round * min(self.player1_score, self.player2_score)
    #
    # def play_next(self):
    #     print(score)
    #     if self.round % 2 == 1:
    #         self.player1 = ((self.player1 + score - 1) % 10) + 1
    #         self.player1_score += self.player1
    #     else:
    #         self.player2 = ((self.player2 + score - 1) % 10) + 1
    #         self.player2_score += self.player2

    # def roll_dice(self):
    #     self.round += 1
    #     return ((self.round - 1) % 100) + 1


def main():
    data = read_data_file_as_lines(21)
    player1 = int(data[0][-1])
    player2 = int(data[1][-1])
    game1 = Game1(player1, player2)
    print("part 1", game1.play())
    game2 = Game2(player1, player2)
    print("part 2", game2.play_from_start())


print((1, 0) + (1, 1))
main()
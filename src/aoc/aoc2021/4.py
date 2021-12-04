from utils import read_data_file_as_lines, chunked, split_to_ints
import numpy as np

data = read_data_file_as_lines(4)


class BingoCard:
    def __init__(self, card: list[list[int]]):
        self.card = np.array(card)

    def lines(self):
        return self.card.tolist() + self.card.T.tolist()

    def is_winner(self, called_nums: list[int]):
        lines = self.lines()
        return any([all([a in called_nums for a in line]) for line in lines])

    def get_nums(self) -> list[int]:
        return list(self.card.flatten())

    def get_score(self, called_nums: list[int]) -> int:
        nums = self.get_nums()
        unmarked_sum = sum([a for a in nums if a not in called_nums])
        return unmarked_sum * called_nums[-1]

    def get_winning_round(self, ordered_nums: list[int]):
        for round in range(len(ordered_nums)):
            called_nums = ordered_nums[:round]
            if self.is_winner(called_nums):
                return round


class BingoGame:
    def __init__(self, cards: list[BingoCard], nums: list[int]):
        self.cards = cards
        self.nums = nums

    def play(self) -> dict:
        results = dict()
        for card in self.cards:
            winning_round = card.get_winning_round(self.nums)
            results[card] = winning_round
        return results

    def get_score_at_round(self, card: BingoCard, round: int):
        return card.get_score(self.nums[:round])


def create_bingo_game(data) -> BingoGame:
    nums = [int(i) for i in data[0].split(',')]

    card_rows = [split_to_ints(a) for a in data[1:] if a != '']
    cards = chunked(card_rows, 5)
    bingo_cards = [BingoCard(card) for card in cards]

    return BingoGame(bingo_cards, nums)


def get_winning_score(game_results):
    card, round = min(list(game_results.items()), key=lambda x: x[1])
    return game.get_score_at_round(card, round)


def get_losing_score(game_results):
    card, round = max(list(game_results.items()), key=lambda x: x[1])
    return game.get_score_at_round(card, round)


game = create_bingo_game(data)
results = game.play()

print("part 1", get_winning_score(results))
print("part 2", get_losing_score(results))

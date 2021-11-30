with open("DataFiles/22.txt") as f:
    data = f.read().replace("Player 1:\n", "").replace(
        "Player 2:\n", "").split("\n\n")

player1 = [int(d) for d in data[0].splitlines()]
player2 = [int(d) for d in data[1].splitlines()]


def playGame(player1, player2):
    gameHistory = []
    while not (len(player1) == 0 or len(player2) == 0):

        for history in gameHistory:
            if player1 == history[0] and player2 == history[1]:
                return [1, player1]

        gameHistory.append([list(player1), list(player2)])

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            winner, hand = playGame(player1[:card1], player2[:card2])
            if winner == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
            continue

        if (card1 > card2):
            player1.append(card1)
            player1.append(card2)
        elif (card1 < card2):
            player2.append(card2)
            player2.append(card1)

    return [1, player1] if len(player1) > 0 else [2, player2]


winner, hand = playGame(player1, player2)

print(winner)
print(sum([(index+1)*value for index, value in enumerate(reversed(hand))]))

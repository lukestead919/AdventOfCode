with open("DataFiles/22.txt") as f:
    data = f.read().replace("Player 1:\n", "").replace("Player 2:\n", "").split("\n\n")

player1 = [int(d) for d in data[0].splitlines()]
player2 = [int(d) for d in data[1].splitlines()]

while not (len(player1) == 0 or len(player2) == 0):
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if (card1 > card2):
        player1.append(card1)
        player1.append(card2)
    elif (card1 < card2):
        player2.append(card2)
        player2.append(card1)

winner = player1 if len(player1) > 0 else player2

print(winner)
print(sum([(index+1)*value for index, value in enumerate(reversed(winner))]))

numberAndTurnLastSpoken = dict()

turn = 1
numbersSpoken = []

with open("DataFiles/15.txt") as f:
    for num in f.read().split(","):
        num = int(num)
        numberAndTurnLastSpoken[num] = turn
        numbersSpoken.append(num)
        lastNum = num
        turn += 1

nextNumToSpeak = 0


while turn <= 2020:
    numToSpeak = nextNumToSpeak
    nextNumToSpeak = 0
    if numberAndTurnLastSpoken.__contains__(numToSpeak):
        nextNumToSpeak = turn - numberAndTurnLastSpoken[numToSpeak]
    numberAndTurnLastSpoken[numToSpeak] = turn
    numbersSpoken.append(numToSpeak)

    turn += 1

# print(numbersSpoken)
print(len(set(numbersSpoken)))
print(numbersSpoken[-1], turn)

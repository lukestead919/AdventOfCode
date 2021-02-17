numberAndTurnLastSpoken = [-1]*30000000

turn = 1
numbersSpoken = [-1]*30000000

with open("DataFiles/15.txt") as f:
    for num in f.read().split(","):
        num = int(num)
        numberAndTurnLastSpoken[num] = turn
        numbersSpoken[turn-1] = num
        lastNum = num
        turn += 1

nextNumToSpeak = 0


while turn <= 30000000:
    numToSpeak = nextNumToSpeak
    nextNumToSpeak = 0
    if numberAndTurnLastSpoken[numToSpeak] > -1:
        nextNumToSpeak = turn - numberAndTurnLastSpoken[numToSpeak]
    numberAndTurnLastSpoken[numToSpeak] = turn
    numbersSpoken[turn-1] = numToSpeak

    turn += 1
    if not turn % 100000:
        print(turn)

# print(numbersSpoken)
print(len(set(numbersSpoken)))
print(numbersSpoken[-1], turn)

import sys
def run_program(seq):
    index = 0

    while True:
        cmd = seq[index]

        if (cmd == 99):
            return seq

        num1 = seq[seq[index+1]]
        num2 = seq[seq[index+2]]
        target = seq[index+3]

        if (cmd == 1):
            newNum = num1 + num2
        elif (cmd == 2):
            newNum = num1 * num2

        seq[target] = newNum

        index += 4


def toList(input):
    return [int(i) for i in input.split(",")]


with open("DataFiles/2.txt") as f:
    input = f.read()

inputListOrig = toList(input)
inputList = list(inputListOrig)
# inputList = run_program(inputList)
inputList[1] = 12
inputList[2] = 2
print(("Part 1:"), run_program(inputList)[0])

for i in range(100):
    for j in range(100):
        inputList = list(inputListOrig)
        inputList[1] = i
        inputList[2] = j
        output = run_program(inputList)[0]
        if output == 19690720:
            print("Part 2:", 100*i + j)
            # sys.exit()
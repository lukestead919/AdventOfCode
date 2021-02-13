import sys

currentLine = 0
gblvar = 0
runLines = set()


def runLine(line):
    command = commands[line].split()
    cmd = command[0]
    global gblvar
    num = int(command[1])
    if cmd == "nop":
        return line + 1
    elif cmd == "acc":
        gblvar += num
        return line + 1
    elif cmd == "jmp":
        return line + num


f = open("DataFiles/8.txt")
commands = f.read().splitlines()

for i in range(len(commands)):
    origCommand = commands[i]
    command = commands[i].split()
    cmd = command[0]
    if cmd == "acc":
        continue
    elif cmd == "nop":
        commands[i] = "jmp " + command[1]
    elif cmd == "jmp":
        commands[i] = "nop " + command[1]

    currentLine = 0
    gblvar = 0
    runLines = set()

    while not runLines.__contains__(currentLine):
        if (currentLine > len(commands)):
            break
        if (currentLine == len(commands)):
            print(gblvar, i, origCommand)
            sys.exit()
        runLines.add(currentLine)
        currentLine = runLine(currentLine)

    commands[i] = origCommand

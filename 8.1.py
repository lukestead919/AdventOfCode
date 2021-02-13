f = open("DataFiles/8.txt")
commands = f.read().splitlines()
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


while not runLines.__contains__(currentLine):
    runLines.add(currentLine)
    currentLine = runLine(currentLine)

print(gblvar)

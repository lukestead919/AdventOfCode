def findClosingBracket(equ):
    numOfOpen = 0
    numOfClosed = 0
    for index, char in enumerate(equ):
        if char == "(":
            numOfOpen += 1
        elif char == ")":
            numOfClosed += 1
            if numOfOpen == numOfClosed:
                return index


def getIndexOfNextOperator(equ, operators):
    retval = min(equ.find(o) if o in equ else 1000000 for o in operators)
    if retval == 1000000:
        retval = -1
    return retval


def solveEquation(equ):
    equ = passEquation(equ, ["+"])
    equ = passEquation(equ, ["*"])
    return equ


def passEquation(equ, operators):

    # find the first open bracket, and solve it
    indexOfBracket = equ.find("(")
    while not indexOfBracket == -1:
        indexOfClosingBracket = findClosingBracket(equ)
        solved = solveEquation(equ[indexOfBracket+1:indexOfClosingBracket])
        equ = equ[:indexOfBracket] + solved + equ[indexOfClosingBracket+1:]
        indexOfBracket = equ.find("(")

    # while equ[0] == "(":
    #     indexOfClosingBracket = findClosingBracket(equ)
    #     solved = solveEquation(equ[1:indexOfClosingBracket])
    #     equ = solved + equ[indexOfClosingBracket+1:]

    indexOfOperator = getIndexOfNextOperator(equ, operators)
    if indexOfOperator == -1:
        return equ

    indexOfPreviousOperator = -1
    try:
        indexOfPreviousOperator = max(index for index, c in enumerate(
            equ[:indexOfOperator]) if not c.isnumeric())
        num1 = int(equ[indexOfPreviousOperator+1:indexOfOperator])
    except:
        num1 = int(equ[:indexOfOperator])

    operation = equ[indexOfOperator]

    # if next is a bracket, solve the equation within the bracket, and replace
    # if equ[indexOfOperator+1] == "(":
    #     indexOfClosingBracket = findClosingBracket(equ)
    #     solved = solveEquation(equ[indexOfOperator+2: indexOfClosingBracket])
    #     equ = equ[:indexOfOperator+1] + \
    #         str(solved) + equ[indexOfClosingBracket+1:]

    # find the index of the next operator, as that will mark the end of num2
    indexOfOperator2 = -1
    try:
        indexOfOperator2 = min(index for index, c in enumerate(
            equ[indexOfOperator+1:]) if not c.isnumeric()) + 1 + indexOfOperator
        num2 = int(equ[indexOfOperator+1:indexOfOperator2])
    except:
        num2 = int(equ[indexOfOperator+1:])

    if operation == "*":
        num = num1*num2
    elif operation == "+":
        num = num1+num2

    retval = str(num)
    if not indexOfOperator2 == -1:
        retval = retval + equ[indexOfOperator2:]
    if not indexOfPreviousOperator == -1:
        retval = equ[:indexOfPreviousOperator+1] + retval

    return solveEquation(retval)


with open("DataFiles/18.txt") as f:
    equns = f.read().replace(" ", "").splitlines()

# print(equns)
retval = 0
for equ in equns:
    retval += int(solveEquation(equ))

print(retval)



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


def getIndexOfNextOperator(equ):
    retval = min(equ.find(o) if o in equ else 1000000 for o in ["+", "*"])
    if retval == 1000000:
        retval = -1
    return retval

def solveEquation(equ):
    while equ[0] == "(":
        indexOfClosingBracket = findClosingBracket(equ)
        equ = equ[1:indexOfClosingBracket] + equ[indexOfClosingBracket+1:]

    indexOfOperator = getIndexOfNextOperator(equ)
    if indexOfOperator == -1:
        return int(equ)

    num1 = int(equ[:indexOfOperator])
    operation = equ[indexOfOperator]

    # if next is a bracket, solve the equation within the bracket, and replace
    if equ[indexOfOperator+1] == "(":
        indexOfClosingBracket = findClosingBracket(equ)
        solved = solveEquation(equ[indexOfOperator+2: indexOfClosingBracket])
        equ = equ[:indexOfOperator+1] + str(solved) + equ[indexOfClosingBracket+1:]

    # find the index of the next operator, as that will mark the end of num2
    indexOfOperator2 = getIndexOfNextOperator(equ[indexOfOperator+1:])
    if indexOfOperator2 > -1:
        indexOfOperator2 += indexOfOperator+1

    if indexOfOperator2 == -1:
        num2 = int(equ[indexOfOperator+1:])
    else:
        num2 = int(equ[indexOfOperator+1:indexOfOperator2])

    if operation == "*":
        num = num1*num2
    elif operation == "+":
        num = num1+num2

    if indexOfOperator2 == -1:
        return int(num)
    else:
        return solveEquation(str(num) + equ[indexOfOperator2:])


with open("DataFiles/18.txt") as f:
    equns = f.read().replace(" ", "").splitlines()

# print(equns)
retval = 0
for equ in equns:
    retval += solveEquation(equ)

print(retval)

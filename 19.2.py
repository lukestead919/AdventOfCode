def getValidMessagesForRule(ruleNum):
    validMessages = []
    r = rules[ruleNum]
    options = r.split(" | ")
    for o in options:
        if o == '"a"':
            validMessages.append("a")
        elif o == '"b"':
            validMessages.append("b")
        else:
            subRules = o.split(" ")
            messages = [""]
            for s in subRules:
                subMessages = getValidMessagesForRule(s)
                messages = [m + s for m in messages for s in subMessages]
            validMessages += messages

    return validMessages


def patternMatches(m):
    if len(m) % 8 == 0:
        splitMessage = [m[8*i:8*(i+1)] for i in range(len(m)//8)]

        countm42 = 0
        countm31 = 0
        for m in splitMessage:
            if countm31 == 0 and m in messages42:
                countm42 += 1
            elif m in messages31:
                countm31 += 1
            else:
                return False
        if countm42 > countm31 and splitMessage[-1] in messages31:
            return True

    return False


with open("DataFiles/19.txt") as f:
    rules, messages = [d.splitlines() for d in f.read().split("\n\n")]
    rules = dict(r.split(": ") for r in rules)

    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"

    # print(rules)
    # print(messages)

messages31 = getValidMessagesForRule("31")
messages42 = getValidMessagesForRule("42")

# print(messages31)
# print(messages42)

retval = 0
for index, m in enumerate(messages):
    # print(index, m)
    if patternMatches(m):
        retval += 1

print(retval)

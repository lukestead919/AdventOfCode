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



with open("DataFiles/19.txt") as f:
    rules, messages = [d.splitlines() for d in f.read().split("\n\n")]
    rules = dict(r.split(": ") for r in rules)
    # print(rules)
    # print(messages)

validMessagesForRules = dict()

# print(getValidMessagesForRule('0'))
validMessages = getValidMessagesForRule('0')
print(len(validMessages))
print(len([m for m in messages if m in validMessages]))

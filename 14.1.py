mask = ""

mem = dict()


def applyMaskToValue(value):
    bValue = format(int(value), 'b')
    bValue = bValue.zfill(len(mask))  # write in binary, padded with 0s
    z = zip(bValue, mask)
    return ''.join([m if not m == "X" else b for b, m in z])


with open("DataFiles/14.txt") as f:
    commands = f.read().splitlines()

for command in commands:
    action, value = command.split(" = ")
    if action == "mask":
        mask = value
    elif action.startswith("mem"):
        memAddress = action[action.find("[")+1: action.find("]")]
        mem[memAddress] = applyMaskToValue(value)

print(sum([int(v, 2) for v in mem.values()]))

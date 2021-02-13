import itertools
mask = ""

mem = dict()


def applyValueToAllMemAddresses(memAddress, value):
    value = int(value)
    # print(memAddress)
    bAddress = format(int(memAddress), 'b')
    # print(bAddress)
    bAddress = bAddress.zfill(len(mask))  # write in binary, padded with 0s
    # print(bAddress)
    z = zip(bAddress, mask)
    maskedAddress = ''.join([m if not m == "0" else b for b, m in z])
    # print(maskedAddress)
    lsts = [['0', '1'] if c == "X" else c for c in maskedAddress]
    # print(lsts)
    for address in itertools.product(*lsts):
        # print(address, list(address))
        # print(address)
        address = ''.join(list(address))
        # print(address)
        address = int(address, 2)
        # print(address)
        mem[address] = value


with open("DataFiles/14.txt") as f:
    commands = f.read().splitlines()

for index, command in enumerate(commands):
    action, value = command.split(" = ")
    if action == "mask":
        mask = value
        # print("Mask Changed")
    elif action.startswith("mem"):
        memAddress = action[action.find("[")+1: action.find("]")]
        applyValueToAllMemAddresses(memAddress, value)
    else:
        print("error")
# print(mem)
# vals = list(mem.values())
# for v in vals:
#     print(v)
print(len(mem))
print(sum(mem.values()))

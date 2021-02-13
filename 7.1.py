from typing import Counter


bagMap = dict()

with open("DataFiles/7.txt") as f:
    for line in f:
        s = line.strip().replace(" bags", "").replace(
            " bag", "").replace(".", "").split(" contain ")
        # print(s)
        contents = dict()
        if (s[1] != "no other"):
            contents = dict([reversed(c.strip().split(" ", 1))
                             for c in s[1].split(",")])
            # print(contents)

        bagMap[s[0]] = contents
        # print(bagMap)

# print(bagMap)


def containsShinyGoldBackRecursive(bag):
    interiorBags = bagMap[bag]
    for iBag in interiorBags.keys():
        if iBag == "shiny gold":
            return True
        if containsShinyGoldBackRecursive(iBag):
            return True
    return False


retval = 0
for bag in bagMap.keys():
    if containsShinyGoldBackRecursive(bag):
        retval += 1
print(retval)

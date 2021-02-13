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


def getNumberOfBagsInBag(bag):
    numOfBags = 0
    interiorBags = bagMap[bag]
    for iBag in interiorBags.keys():
        numOfBags += (getNumberOfBagsInBag(iBag) + 1) * int(interiorBags[iBag])
    return numOfBags


print(getNumberOfBagsInBag("shiny gold"))

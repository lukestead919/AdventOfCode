from os import replace


with open("DataFiles/13.txt") as f:
    file = f.read().splitlines()
    target = int(file[0])
    buses = [int(b) for b in file[1].replace(",x", "").split(",")]

busAndTimeToWait = dict([[bus, bus - target % bus] for bus in buses])

minTimeToWait = min(busAndTimeToWait.values())
print(busAndTimeToWait)
bestBus = min(busAndTimeToWait, key=busAndTimeToWait.get)
print(bestBus, busAndTimeToWait[bestBus], bestBus * busAndTimeToWait[bestBus])

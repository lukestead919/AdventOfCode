from os import replace


with open("DataFiles/13.txt") as f:
    file = f.read().splitlines()
    buses = [b for b in file[1].split(",")]


buses = dict([[int(bus), buses.index(bus)] for bus in buses if not bus == "x"])
print(buses)
t = 0
busNumbers = list(buses.keys())
product = busNumbers[0]
for bus in busNumbers[1:]:
    while not (t + buses[bus]) % bus == 0:
        t += product
        # print(t)
    product *= bus
    print("done. ", str(t), str(product))

print(t % product)

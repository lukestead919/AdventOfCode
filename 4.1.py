requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

currentPassport = dict()
retval = 0

with open("DataFiles/4.txt") as f:
    for line in f:
        if line == "\n":
            # print(currentPassport)
            if all(field in currentPassport.keys() for field in requiredFields):
                retval += 1
                # print(" was good!")
            currentPassport = dict()

        fields = line.split()
        for field in fields:
            (key, value) = field.split(":")
            currentPassport[key] = value

if all(field in currentPassport.keys() for field in requiredFields):
    retval += 1
    # print(" was good!")
currentPassport = dict()

print(retval)

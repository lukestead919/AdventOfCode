requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

currentAnswers = set()
retval = 0

with open("DataFiles/6.txt") as f:
    for line in f:
        if line == "\n":
            retval += len(currentAnswers)
            # print(currentAnswers)
            currentAnswers = set()

        for char in line:
            if char.isalpha():
                currentAnswers.add(char)

retval += len(currentAnswers)

print(retval)

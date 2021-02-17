requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

currentAnswers = None
retval = 0

with open("DataFiles/6.txt") as f:
    for line in f:
        if line == "\n":
            retval += len(currentAnswers)
            # print(currentAnswers)
            currentAnswers = None
            continue

        personsAnswers = set()
        for char in line:
            if char.isalpha():
                personsAnswers.add(char)

        # print(currentAnswers, line, personsAnswers)

        if currentAnswers == None:
            currentAnswers = personsAnswers
        else:
            currentAnswers = currentAnswers.intersection(personsAnswers)

        # print(currentAnswers)

retval += len(currentAnswers)

print(retval)

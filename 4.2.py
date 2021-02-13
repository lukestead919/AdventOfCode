from string import hexdigits
import re

validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def isPassportValid(passport):

    if not all(field in passport.keys() for field in requiredFields):
        return False

    try:
        byr = int(passport["byr"])
        if not (byr >= 1920 and byr <= 2002):
            return False

        iyr = int(passport["iyr"])
        if not (iyr >= 2010 and iyr <= 2020):
            return False

        eyr = int(passport["eyr"])
        if not (eyr >= 2020 and eyr <= 2030):
            return False

        hgt = passport["hgt"]
        s = re.split('([a-z]+)', hgt)
        if len(s) < 2:
            return False
        value = int(s[0])
        unit = s[1]
        if not (unit == "cm" and (value >= 150 and value <= 193)
                or unit == "in" and (value >= 59 and value <= 76)):
            return False

        hcl = passport["hcl"]
        if not (hcl[0] == "#" and all(c in hexdigits for c in hcl[1:])):
            return False

        ecl = passport["ecl"]
        if not (ecl in validEcl):
            return False

        pid = passport["pid"]
        if not (pid.isnumeric() and len(pid) == 9):
            return False

        return True
    except:
        return False


currentPassport = dict()
retval = 0

with open("DataFiles/4.txt") as f:
    for line in f:
        if line == "\n":
            # print(currentPassport)
            if isPassportValid(currentPassport):
                retval += 1
                # print(" was good!")
            currentPassport = dict()

        fields = line.split()
        for field in fields:
            (key, value) = field.split(":")
            currentPassport[key] = value

if isPassportValid(currentPassport):
    retval += 1

print(retval)

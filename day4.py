import re

class Passport(object):
    def __init__(self):
        self.fields = {}

    def setfield(self, key, val):
        self.fields[key] = val

    def isvalid(self):
        required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for key in required_keys:
            if key not in self.fields:
                return False

        return True


def read_input(file_name):
    file = open(file_name, 'r')
    raw_passport = ""
    passports = set()

    line: str
    for line in file.readlines():
        if "\n" == line:
            entries = raw_passport.strip().split(" ")
            raw_passport = ""
            passport = Passport()
            for entry in entries:
                [key, value] = entry.split(":")
                passport.setfield(key, value)
            passports.add(passport)
        else:
            raw_passport = raw_passport + " " + line.strip()

    return passports


def count_valid(passports):
    valid = 1
    for passport in passports:
        if passport.isvalid():
            valid = valid + 1

    return valid


if __name__ == '__main__':
    passports = read_input('input_day4.txt')
    result = count_valid(passports)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

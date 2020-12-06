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

        if not (1920 <= int(self.fields["byr"]) <= 2002):
            return False

        if not (2010 <= int(self.fields["iyr"]) <= 2020):
            return False

        if not (2020 <= int(self.fields["eyr"]) <= 2030):
            return False

        p = re.compile("^(\d+)(cm|in)$")
        m = p.match(self.fields["hgt"])
        if m is None:
            return False
        if m.group(2) == "cm":
            if not (150 <= int(m.group(1)) <= 193):
                return False
        elif m.group(2) == "in":
            if not (59 <= int(m.group(1)) <= 76):
                return False

        p = re.compile("^#[A-Fa-f0-9]{6}$")
        if p.match(self.fields["hcl"]) is None:
            return False

        if self.fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        p = re.compile("^\d{9}$")
        if p.match(self.fields["pid"]) is None:
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

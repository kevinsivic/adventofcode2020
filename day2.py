import re

class Password(object):
    def __init__(self):
        self.pos1 = -1
        self.pos2 = -1
        self.char = '-1'
        self.password = '-1'

    def setpos1(self, pos1):
        self.pos1 = int(pos1)

    def setpos2(self, pos2):
        self.pos2 = int(pos2)

    def setchar(self, char):
        self.char = char

    def setpass(self, password):
        self.password = password


def read_input(file_name):
    file = open(file_name, 'r')
    data = set()
    p = re.compile('(\d+)-(\d+) (\w): (.+)')
    for entry in file.readlines():
        m = p.match(entry)
        password = Password()
        password.setpos1(m.group(1))
        password.setpos2(m.group(2))
        password.setchar(m.group(3))
        password.setpass(m.group(4))
        
        data.add(password)

    return data


def calculate_day2(data):
    valid = 0
    for password in data:
        pos1 = password.pos1
        pos2 = password.pos2
        char = password.char
        password = password.password
        if (password[pos1-1] == char) ^ (password[pos2-1] == char):
            valid += 1

    return valid


if __name__ == '__main__':
    data = read_input('input_day2.txt')
    result = calculate_day2(data)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

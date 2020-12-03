import re

class Password(object):
    def __init__(self):
        self.min = -1
        self.max = -1
        self.char = '-1'
        self.password = '-1'

    def setmin(self, min):
        self.min = int(min)

    def setmax(self, max):
        self.max = int(max)

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
        password.setmin(m.group(1))
        password.setmax(m.group(2))
        password.setchar(m.group(3))
        password.setpass(m.group(4))
        
        data.add(password)

    return data


def calculate_day2(data):
    valid = 0
    for password in data:
        count = password.password.count(password.char)
        if password.max >= count >= password.min:
            valid += 1

    return valid


if __name__ == '__main__':
    data = read_input('input_day2.txt')
    result = calculate_day2(data)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

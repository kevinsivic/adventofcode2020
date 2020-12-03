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
    hill = dict()
    i = 0

    for entry in file.readlines():
        hill[i] = entry
        i += 1

    return hill


def calculate_day3(hill):
    collisions = 0
    x = 0
    max_x = len(hill[0]) - 1 # 0 indexed and remove newline at the end.
    for y in range(0, len(hill)):
        current_loc = hill[y][x]
        if current_loc == '#':
            collisions += 1
        x += 3
        if (x >= max_x):
            x = x - max_x

    return collisions


if __name__ == '__main__':
    hill = read_input('input_day3.txt')
    result = calculate_day3(hill)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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
    coll_a = calc_collisions(hill, 1, 1)
    coll_b = calc_collisions(hill, 3, 1)
    coll_c = calc_collisions(hill, 5, 1)
    coll_d = calc_collisions(hill, 7, 1)
    coll_e = calc_collisions(hill, 1, 2)

    collisions = coll_a * coll_b * coll_c * coll_d * coll_e

    return collisions


def calc_collisions(hill, x_change, y_change):
    collisions = 0
    x = 0
    y = 0
    max_x = len(hill[0]) - 1  # 0 indexed and remove newline at the end.
    while y < len(hill):
        current_loc = hill[y][x]
        if current_loc == '#':
            collisions += 1
        x += x_change
        if x >= max_x:
            x = x - max_x

        y = y + y_change

    return collisions


if __name__ == '__main__':
    hill = read_input('input_day3.txt')
    result = calculate_day3(hill)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

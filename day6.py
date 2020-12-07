def read_input(file_name):
    file = open(file_name, 'r')
    groups = list()
    group = dict()

    line: str
    for line in file.readlines():
        if line == "\n":
            groups.append(group)
            group = dict()
        else:
            for answer in line.strip():
                group[answer] = 1

    groups.append(group)

    return groups


def sum_groups(groups):
    total_yeses = 0

    for group in groups:
        total_yeses = total_yeses + len(group)

    return total_yeses


if __name__ == '__main__':
    groups = read_input('input_day6.txt')
    result = sum_groups(groups)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

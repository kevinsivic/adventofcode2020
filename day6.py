def read_input(file_name):
    file = open(file_name, 'r')
    groups = list()
    group = dict()
    num_members = 0

    line: str
    for line in file.readlines():
        if line == "\n":
            filter_unanimous(group, num_members)
            groups.append(group)
            group = dict()
            num_members = 0
        else:
            num_members = num_members + 1
            for answer in line.strip():
                count = 0
                if answer in group:
                    count = group[answer]
                group[answer] = count + 1

    filter_unanimous(group, num_members)
    groups.append(group)

    return groups


def filter_unanimous(group, num_members):
    for question, count in group.copy().items():
        if count < num_members:
            group.pop(question)


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

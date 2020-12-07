def read_input(file_name):
    file = open(file_name, 'r')
    seats = list()
    row_slice = slice(0, 7)
    column_slice = slice(7, 10)

    line: str
    for line in file.readlines():
        seat = dict()
        seat['row_definition'] = line[row_slice]
        seat['column_definition'] = line[column_slice]
        seats.append(seat)

    return seats


def find_pos(definition):
    definition = definition.replace('L', '0').replace('R', '1')
    definition = definition.replace('F', '0').replace('B', '1')

    return int(definition, 2)


def find_max_seat(seats):
    max_seat = -1

    for seat in seats:
        seat_id = calculate_seat_id(seat)

        if seat_id > max_seat:
            max_seat = seat_id

    return max_seat


def calculate_seat_id(seat):
    column = find_pos(seat['column_definition'])
    row = find_pos(seat['row_definition'])
    seat_id = row * 8 + column
    return seat_id


def find_missing_seat(seats):
    seat_ids = list()
    for seat in seats:
        seat_ids.append(calculate_seat_id(seat))

    seat_ids.sort()
    missing_id = -1

    while len(seat_ids) != 0:
        curr_id = seat_ids.pop(0)
        if curr_id + 1 != seat_ids.pop(0):
            missing_id = curr_id + 1
            seat_ids = list()

    return missing_id

if __name__ == '__main__':
    seats = read_input('input_day5.txt')
    result = find_missing_seat(seats)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def read_input(file_name):
    file = open(file_name, 'r')
    data = set()
    for entry in file.readlines():
        data.add(int(entry))
    return data


def calculate_day1(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                return i*j


if __name__ == '__main__':
    data = read_input('input_day1.txt')
    result = calculate_day1(data)
    print(f'The result is {result}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def swap(info):
    command = info[0]
    first_index = int(info[1])
    second_index = int(info[2])
    numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]

    return numbers


def multiply(info):
    command = info[0]
    first_index = int(info[1])
    second_index = int(info[2])
    numbers[first_index] = numbers[second_index] * numbers[first_index]
    return numbers


def decrease(info):
    new_numbers = [n - 1 for n in numbers]
    return new_numbers



numbers = list(map(int, input().split(' ')))
command_info = input()
while command_info != 'end':
    command_info = command_info.split(' ')
    command = command_info[0]
    if command == 'swap':
        numbers = swap(command_info)
    elif command == 'multiply':
        numbers = multiply(command_info)
    elif command == 'decrease':
        numbers = decrease(command_info)

    command_info = input()

print(', '.join(map(str, numbers)))

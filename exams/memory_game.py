def wrong_numbers(list, moves):
    index_first_num = len(list) // 2
    index_second_num = index_first_num + 1
    list.insert(index_first_num, f"-{moves}a")
    list.insert(index_second_num, f"-{moves}a")
    print("Invalid input! Adding additional elements to the board")
    return list


def matching_elements(first_num, second_num, list, count):
    element = list[first_num]
    if first_num > second_num:
        list.pop(second_num)
        list.pop(first_num - 1)
    else:
        list.pop(first_num)
        list.pop(second_num - 1)
    if len(list) > 0:
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print(f"Congrats! You have found matching elements - {element}!")
        print(f"You have won in {count} turns!")
    return list


def different_elements():
    print("Try again!")


elements = list(map(str, input().split()))
all_elements = [e for e in elements]
number_moves = 1
elements_length = len(all_elements)

while all_elements:
    numbers = input()
    if numbers == 'end':
        print(f"Sorry you lose :(")
        print(f"{' '.join(map(str, all_elements))}")
        break
    else:
        numbers = list(map(int, numbers.split()))
        first_number = int(numbers[0])
        second_number = int(numbers[1])
        if first_number < 0 or second_number < 0 or first_number >= len(all_elements) or second_number >= len(all_elements) or first_number == second_number:
            wrong_numbers(all_elements, number_moves)
            number_moves += 1
        elif all_elements[first_number] == all_elements[second_number]:
            matching_elements(first_number, second_number, all_elements, number_moves)
            number_moves += 1
        elif all_elements[first_number] != all_elements[second_number]:
            different_elements()
            number_moves += 1






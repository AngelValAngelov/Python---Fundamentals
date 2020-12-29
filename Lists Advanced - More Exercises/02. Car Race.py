def car_race(numbers):
    len_num = int((len(numbers) + 1) / 2)

    first_list = numbers[:len_num - 1]
    second_list = numbers[len_num:]

    time_first = 0

    for i in first_list:
        if i != 0:
            time_first += i
        else:
            time_first *= 0.8

    time_second = 0

    for i in reversed(second_list):
        if i != 0:
            time_second += i
        else:
            time_second *= 0.8

    if time_first <= time_second:
        return f"The winner is left with total time: {time_first:.1f}"
    else:
        return f"The winner is right with total time: {time_second:.1f}"


number = list(map(int, input().split(" ")))

print(car_race(number))

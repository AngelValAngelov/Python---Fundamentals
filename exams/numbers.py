numbers = list(map(int, input().split(' ')))
numbers_count = len(numbers)
average_numbers = sum(numbers) / numbers_count
greater_numbers = []
sorted_numbers = sorted(numbers, reverse=True)


if numbers_count >= 5:
    for number in range(len(sorted_numbers)):
        if number < 5 and sorted_numbers[number] > average_numbers:
            greater_numbers.append(sorted_numbers[number])
    if greater_numbers:
        print(' '.join(map(str, greater_numbers)))
    else:
        print('No')
else:
    print('No')

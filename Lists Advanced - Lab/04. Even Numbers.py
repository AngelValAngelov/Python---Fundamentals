numbers = list(map(int, input().split(", ")))
even_numbers = []


def even_num(num):
    global even_numbers
    for i in range(len(num)):
        if num[i] % 2 == 0:
            even_numbers.append(i)

    return even_numbers


print(even_num(numbers))

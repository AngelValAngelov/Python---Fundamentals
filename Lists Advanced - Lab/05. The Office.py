numbers = list(map(int, input().split()))
num = int(input())


def numbers_after_multiplying(n):
    global numbers
    numbers = [numbers[i] * 3 for i in range(len(numbers))]

    return numbers


def average_happiness():
    global numbers
    result = sum(numbers) / len(numbers)

    return result


def happy_people():
    global numbers
    happy_people_list = list()
    happy_people_list = [happy_people_list.append(i) for i in numbers if i >= average_happiness()]

    return happy_people_list


def solve():
    global numbers
    happy_count = len(happy_people())
    total_count = len(numbers)
    if len(happy_people()) >= len(numbers) / 2:
        return f"Score: {happy_count}/{total_count}. Employees are happy!"
    else:
        return f"Score: {happy_count}/{total_count}. Employees are not happy!"


print(solve())

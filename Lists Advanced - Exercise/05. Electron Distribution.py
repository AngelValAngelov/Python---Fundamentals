def solve(number):
    new_list = []

    for i in range(1, number + 1):
        num = 2 * i ** 2
        if number >= sum(new_list) + num:
            new_list.append(num)
            if number == sum(new_list):
                break
        else:
            num = number - sum(new_list)
            new_list.append(num)
            break

    return new_list


n = int(input())

print(solve(n))

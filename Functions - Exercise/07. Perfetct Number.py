def solve():
    for num in range(1, number):
        if number % num == 0:
            list_number.append(num)

    if sum(list_number) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


list_number = []
number = int(input())

solve()

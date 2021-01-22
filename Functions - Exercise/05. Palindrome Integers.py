def solve():
    for number in num:
        nums = number
        numbers = int(str(number)[::-1])
        if int(numbers) == int(nums):
            is_number = True
            print(is_number)
        else:
            is_number = False
            print(is_number)

num = input().split(", ")
is_number = True

solve()
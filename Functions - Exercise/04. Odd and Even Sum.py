big_number = input()

def solve():
    odd_number = 0
    even_number = 0
    for digit in big_number:
        digit = int(digit)
        if digit % 2 == 0:
            even_number += digit
        else:
            odd_number += digit

    print(f"Odd sum = {odd_number}, Even sum = {even_number}")

solve()
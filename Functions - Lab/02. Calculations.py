def solve(sign, number_1, number_2):
    def is_multiply(number_1, number_2):
        result = int(number_1 * number_2)
        return result

    def is_divide(number_1, number_2):
        result = number_1 // number_2
        return result

    def is_add(number_1, number_2):
        result = number_1 + number_2
        return result

    def is_subtract(number_1, nummber_2):
        result = number_1 - number_2
        return result

    if sign == 'multiply':
        return is_multiply(number_1, number_2)
    elif sign == 'divide':
        return is_divide(number_1, number_2)
    elif sign == 'add':
        return is_add(number_1, number_2)
    elif sign == 'subtract' :
        return is_subtract(number_1, number_2)


sign = input()
number_1 = int(input())
number_2 = int(input())

print(solve(sign, number_1, number_2))

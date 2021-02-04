def integer_to_base(number, to_base):
    result = []
    while number != 0:
        n = number % to_base
        result.append(n)
        b = number // to_base
        result.append(b)
        print(str(result))



num = int(input())
base = int(input())

integer_to_base(num, base)
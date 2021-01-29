import math


def solve():
    a = int(input())
    b = int(input())

    a = math.factorial(a)
    b = math.factorial(b)
    c = a / b

    print(f"{c:.2f}")


solve()

def coffee(q):
    result = 1.50 * q
    return f"{result:.2f}"


def water(q):
    result = 1.00 * q
    return f"{result:.2f}"


def coke(q):
    result = 1.40 * q
    return f"{result:.2f}"


def snacks(q):
    result = 2.00 * q
    return f"{result:.2f}"


product = input()
quantity = int(input())

if product == "coffee":
    print(coffee(quantity))
elif product == "water":
    print(water(quantity))
elif product == "coke":
    print(coke(quantity))
elif product == "snacks":
    print(snacks(quantity))
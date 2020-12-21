def solve():
    numbers.sort()
    numbers.reverse()
    print("".join(numbers))


numbers = input().split()

solve()
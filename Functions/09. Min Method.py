def get_min(a, b, c):
    if a < b < c:
        print(a)
    elif b < a < c:
        print(b)
    else:
        print(c)


get_min(int(input()), int(input()), int(input()))

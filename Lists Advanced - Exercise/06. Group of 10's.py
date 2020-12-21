def solve():
    nn_list = list(map(int, input().split(", ")))
    print(nn_list)
    lists = 0

    while len(nn_list) > 0:
        lists += 10
        nummm = [x for x in nn_list if x <= lists]
        nn_list = [x for x in nn_list if x > lists]
        print(f"Group of {lists}'s: {nummm}")


solve()

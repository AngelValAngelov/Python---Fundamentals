def solve():
    percent_loaded = []
    for num in range(1, number + 1):
        if num % 10 == 0:
            percent_loaded.append("%")

    new_str = 10 - len(percent_loaded)
    new_s = ["."] * new_str
    all_percent = percent_loaded + new_s
    ready = "".join(all_percent)
    run = []
    run.append(ready)
    run = "".join(run)

    if len(percent_loaded) == 10:
        print("100% Complete!")
        print(f"[{run}]")
    else:
        print(f"{number}% [{run}]")
        print("Still loading...")
number = int(input())


solve()

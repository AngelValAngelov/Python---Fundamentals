def repeat_str(str, count):
    for i in range(count):
        print(f"{str}", end="")

string = input()
number = int(input())

repeat_str(string, number)
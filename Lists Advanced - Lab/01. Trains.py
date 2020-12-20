wagons = list()


def wags(num):
    global wagons
    for i in range(num):
        wagons.append(0)
    return wagons


def add(num):
    global wagons
    wagons[-1] += int(num)
    return wagons


def insert(poss, num):
    global wagons
    wagons[int(poss)] = wagons[int(poss)] + int(num)
    return wagons


def leave(poss, num):
    global wagons
    wagons[int(poss)] = wagons[int(poss)] - int(num)
    return wagons


numbers_of_wagons = int(input())
wags(numbers_of_wagons)
command = input()


def solve():
    global command
    while command != "End":
        command = command.split()
        args = command[0]
        if args == "add":
            people = command[1]
            add(people)
        elif args == "insert":
            wagon = command[1]
            people = command[2]
            insert(wagon, people)
        else:
            wagon = command[1]
            people = command[2]
            leave(wagon, people)
        command = input()

    return wagons


print(solve())

def add(tour, old, new):
    if int(old) >= 0 and len(tour) > int(old):
        t = tour[:int(old)] + new + tour[int(old):]
        print(t)
        return t
    print(tour)
    return tour


def remove(tour, old, new):
    if int(old) >= 0 and int(new) >= 0 and len(tour) > int(new):
        new_tour = tour[:int(old)] + tour[int(new) + 1:]
        print(new_tour)
        return new_tour
    print(tour)
    return tour


def switch(tour, old, new):
    if old in tour:
        new_tour = tour.replace(old, new)
        print(new_tour)
        return new_tour
    print(tour)
    return tour


tour = input()
destination = input()

while destination != 'Travel':
    destination = destination.replace(':', ' ')
    act_todos = destination.split(' ')
    command = act_todos[0]

    if command == 'Add':
        act = act_todos[1]
        old_index = act_todos[2]
        new_index = act_todos[3]
        tour = add(tour, old_index, new_index)
    elif command == 'Remove':
        act = act_todos[1]
        old_index = act_todos[2]
        new_index = act_todos[3]
        tour = remove(tour, old_index, new_index)
    elif command == 'Switch':
        old_index = act_todos[1]
        new_index = act_todos[2]
        tour = switch(tour, old_index, new_index)

    destination = input()

print(f'Ready for world tour! Planned stops: {tour}')


def shoot(targets, idx, val):
    if idx in range(len(targets)):
        targets[idx] -= val
        if targets[idx] <= 0:
            targets.pop(idx)
    return targets


def add(targets, idx, val):
    if idx in range(len(targets)):
        targets.insert(idx, val)
    else:
        print("Invalid placement!")
    return targets


def strike(targets, idx, val):
    if idx in range(len(targets)) and idx - val in range(len(targets)) and idx + val in range(len(targets)):
        new_targets = targets[:idx - val] + targets[idx + val + 1:]
        return new_targets
    print("Strike missed!")
    return targets


targets = list(map(int, input().split()))

command = input()

while command != 'End':
    command = command.split()
    act = command[0]
    index = int(command[1])
    value = int(command[2])

    if act == 'Shoot':
        targets = shoot(targets, index, value)
    elif act == 'Add':
        targets = add(targets, index, value)
    elif act == 'Strike':
        targets = strike(targets, index, value)

    command = input()

targets = [str(t) for t in targets]
print('|'.join(targets))

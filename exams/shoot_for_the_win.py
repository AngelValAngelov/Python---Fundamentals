targets = list(map(int, input().split()))
target_numbers = len(targets)
shot = input()

while shot != 'End':
    shot = int(shot)
    if shot < target_numbers:
        current_target = targets[shot]
        targets[shot] = -1
        for target in range(target_numbers):
            if targets[target] < 0:
                continue
            if targets[target] <= current_target:
                targets[target] += current_target
            else:
                targets[target] -= current_target
                if targets[target] < 0:
                    targets[target] = -1

    shot = input()

shooted_targets = len([t for t in targets if t < 0])
print(f"Shot targets: {shooted_targets} -> {' '.join(map(str, targets))}")

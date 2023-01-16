people_count = int(input())
lift_capacity_input = list(map(int, input().split()))
lift = [c for c in lift_capacity_input]
wagon_capacity = 4
current_wagon = 0

for wagon in lift_capacity_input:
    if wagon < wagon_capacity:
        if people_count >= wagon_capacity:
            free_spots_in_current_wagon = wagon_capacity - wagon
            lift[current_wagon] += free_spots_in_current_wagon
            people_count -= free_spots_in_current_wagon
        else:
            lift[current_wagon] += people_count
            people_count = 0
    current_wagon += 1

if people_count == 0 and [w for w in lift if w != 4]:
    print("The lift has empty spots!")
elif people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
print(' '.join(map(str, lift)))

energy = int(input())
distance = input()
points = 0
beat_all_enemies = False

if distance == "End of battle":
    beat_all_enemies = True

while distance != "End of battle":
    distance = int(distance)

    if energy - distance < 0:
        break

    energy -= distance
    points += 1

    if points % 3 == 0:
        energy += points

    distance = input()
    if distance == "End of battle":
        beat_all_enemies = True
        break

if beat_all_enemies:
    print(f'Won battles: {points}. Energy left: {energy}')
else:
    print(f'Not enough energy! Game ends with {points} won battles and {energy} energy')


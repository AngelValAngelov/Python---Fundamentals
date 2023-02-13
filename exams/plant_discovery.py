def rate(plants, name, rarity):
    find = False
    for plant in plants:
        if plant[0] == name:
            plant[2].append(int(rarity))
            find = True
    if not find:
        print('error')
    return plants


def update(plants, name, rarity):
    find = False
    for plant in plants:
        if plant[0] == name:
            plant[1] = rarity
            find = True
    if not find:
        print('error')
    return plants


def reset(plants, name):
    find = False
    for plant in plants:
        if plant[0] == name:
            plant[2] = []
            find = True
    if not find:
        print('error')
    return plants

number_of_plants = int(input())
plants = []

# for plant in range(number_of_plants):
#     plants.append(input())


[plants.append(input().split('<->')) for _ in range(number_of_plants)]
[plant.append([]) for plant in plants]
act = input()

while act != 'Exhibition':
    commands = act.split(' ')
    todo = commands[0][:-1]
    plant_name = commands[1]
    if todo == 'Rate':
        plant_rarity = commands[-1]
        plants = rate(plants, plant_name, plant_rarity)
    elif todo == 'Update':
        plant_rarity = commands[-1]
        plants = update(plants, plant_name, plant_rarity)
    elif todo == 'Reset':
        plants = reset(plants, plant_name)

    act = input()

print("Plants for the exhibition:")
print('\n'.join([f'- {n[0]}; Rarity: {n[1]}; Rating: '
                 f'{ 0.00 if len(n[2]) == 0 else sum(n[2]) / len(n[2]):.2f}'
                 for n in plants]))

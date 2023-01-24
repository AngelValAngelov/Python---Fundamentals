import re


def participant_name(chars):
    name = r'[A-Za-z]'
    matches = re.findall(name, chars)
    participant_name = ''
    for letter in matches:
        participant_name += letter
    return participant_name


def participant_distance(chars):
    distance = r'[0-9]'
    matches = re.findall(distance, chars)
    participant_distance = 0
    for digit in matches:
        participant_distance += int(digit)
    return participant_distance


participants = input().split(', ')
rank_list = {}
characters = input()
name = ''
distance = 0

while characters != 'end of race':
    name = participant_name(characters)
    distance = participant_distance(characters)
    if name in participants:
        if name in rank_list.keys():
            rank_list[name] += distance
        else:
            rank_list[name] = distance
    distance = 0
    characters = input()

final_ranking = {k: v for k, v in sorted(rank_list.items(), key=lambda item: -item[1])}

print(f'1st place: {list(final_ranking.keys())[0]}')
print(f'2nd place: {list(final_ranking.keys())[1]}')
print(f'3rd place: {list(final_ranking.keys())[2]}')

import re

names = input().split(', ')

damage_pattern = r'(?P<number>(-*)[0-9\.0-9]+|[0-9]+)'
multiply_damage_pattern = r'(?P<multiply>\*)'
health_pattern = r'(?P<letter>[A-Za-z])'
heroes = {}

for name in names:
    matches = re.finditer(damage_pattern, name)
    multiply_damage_matches = re.finditer(multiply_damage_pattern, name)
    health = re.finditer(health_pattern, name)
    multiply_damage = len([match.group('multiply') for match in multiply_damage_matches])
    damage = sum([float(match.group('number')) for match in matches])
    damage *= (len([x for x in range(multiply_damage)])) * 2
    health_points = sum([ord(match.group('letter')) for match in health])
    hero_info = [health_points, damage]
    heroes[name] = hero_info

for hero, info in sorted(heroes.items()):
    print(f"{hero} - {info[0]} health, {info[1]:.2f} damage")

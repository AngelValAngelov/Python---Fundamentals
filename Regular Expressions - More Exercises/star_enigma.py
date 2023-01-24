import re

message_count = int(input())

new_message = ''
pattern = r'[star]'
# planet_name_pattern = r'[^@!:>-]*@(?P<planet>[A-Za-z]+)'
# planet_population_pattern = r'[^@!:>-]*:(?P<population>[0-9]+)'
# attack_type_pattern = r'[^@!:>-]*!(?P<attack_type>A|D)!'
# soldiers_count_pattern = r'[^@!:>-]*->(?P<soldiers>[0-9]+)'
planet_pattern = r'[^@!:>-]*@(?P<planet>[A-Za-z]+)[^@!:>-]*:(?P<population>[0-9]+)[^@!:>-]*!(?P<attack_type>A|D)![^@!:>-]*->(?P<soldiers>[0-9]+)'
attacked_planets = []
destroyed_planets = []

for _ in range(message_count):
    message = input()
    decryption_key = len(re.findall(pattern, message, re.IGNORECASE))
    for letter in message:
        new_message += chr(ord(letter)-decryption_key)
    attack_type = [a.group('attack_type') for a in re.finditer(planet_pattern, new_message)]
    planet_name = [p.group('planet') for p in re.finditer(planet_pattern, new_message)]
    planet_population = [p.group('population') for p in re.finditer(planet_pattern, new_message)]
    soldiers_count = [p.group('soldiers') for p in re.finditer(planet_pattern, new_message)]
    if attack_type and planet_name and planet_population and soldiers_count:
        if attack_type == ['A']:
            attacked_planets.append(planet_name)
        elif attack_type == ['D']:
            destroyed_planets.append(planet_name)
    new_message = ''
    attack_type = ''
    planet_name = ''
    planet_population = ''
    soldiers_count = ''

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {''.join(planet)}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {''.join(planet)}")


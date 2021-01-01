key_material = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk_items = {}
winner = ""
while winner == "":
    items = input().lower().split()
    for i in range(0, len(items), 2):
        key = items[i + 1]
        value = int(items[i])
        if key in key_material:
            key_material[key] += value
            if key_material[key] >= 250:
                winner = key
                key_material[winner] -= 250
                break
        elif key in junk_items:
            junk_items[key] += value
        elif key not in junk_items:
            junk_items[key] = value
        else:
            junk_items[key] += value


print(f"{legendary_items[winner]} obtained!")

sorted_dict = dict(sorted(key_material.items(), key=lambda el:(-el[1], el[0])))
sorted_junk = dict(sorted(junk_items.items()))

for key, value in sorted_dict.items():
    print(f"{key}: {value}")
for key, value in sorted_junk.items():
    print(f"{key}: {value}")
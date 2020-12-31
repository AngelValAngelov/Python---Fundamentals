def bakery(data):
    for i in range(0, len(elements), 2):
        key = elements[i]
        value = int(elements[i + 1])
        last_dict[key] = value
    return last_dict


last_dict = {}
elements = input().split()

print(bakery(last_dict))
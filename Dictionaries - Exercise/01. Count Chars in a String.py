text = input()

dictionary = {}

for letter in text:
    if letter != " ":
        if letter not in dictionary.keys():
            dictionary[letter] = 0
        dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
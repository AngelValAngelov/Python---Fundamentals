number = int(input())
dictionary = {}

while number > 0:
    word = input()
    sinonim = input()
    if word not in dictionary:
        dictionary[word] = []
    if sinonim not in dictionary[word]:
        dictionary[word].append(sinonim)
    number -= 1

for (key, value) in dictionary.items():
    print(f"{key} - {', '.join(value)}")

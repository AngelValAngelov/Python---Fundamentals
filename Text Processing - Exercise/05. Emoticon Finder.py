text = input()

for letter in range(len(text)):
    if text[letter] == ":":
        if not(text[letter + 1].isspace()):
            print(f"{text[letter]}{text[letter + 1]}")
string = input()
damage = 0

for letter in range(len(string)):
    if string[letter] == ">":
        print(string[letter],end="")
        damage += int(string[letter + 1])
    else:
        if damage == 0:
            print(string[letter], end="")
        else:
            damage -= 1



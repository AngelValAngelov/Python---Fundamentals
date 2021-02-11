string = input()

for ch in string:
    char = ord(ch) + 3
    print(chr(char), end="")

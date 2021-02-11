string = input()

previos_letter = "" \
                 ""
for ch in range(len(string)):
    if string[ch] != previos_letter:
        print(string[ch], end="")
        previos_letter = string[ch]
list_tickets = [i.strip() for i in input().split(", ")]

counter = 0
best_counter = 0
spesial_sign = ""
best_spesial_sign = ""
count = 0
best_count = 0
spesial_s = ""
best_special_s = ""
for word in list_tickets:
    if len(word) != 20:
        print(f"invalid ticket")
        continue
    co = 1
    for letter in word:
        first_half = len(word) / 2
        if letter == "@":
            spesial_sign = "@"
        if letter == "#":
            spesial_sign = "#"
        if letter == "$":
            spesial_sign = "$"
        if letter == "^":
            spesial_sign = "^"
        if spesial_sign != "":
            if spesial_sign == letter:
                counter += 1
                if counter >= best_counter:
                    best_counter = counter
                    best_spesial_sign = letter
            else:
                counter = 0
        if co == first_half:
            break
        co += 1

    c = 1
    for lett in reversed(word):
        second_half = len(word) / 2
        if lett == "@":
            spesial_s = "@"
        if lett == "#":
            spesial_s = "#"
        if lett == "$":
            spesial_s = "$"
        if lett == "^":
            spesial_s = "^"
        if spesial_s != "":
            if spesial_s == lett:
                count += 1
                if count >= best_count:
                    best_count = count
                    best_spesial_s = lett
            else:
                count = 0
        if c == second_half:
            break
        c += 1

    if best_counter == best_count and spesial_sign == spesial_s:
        if best_counter == 10:
            print(f'ticket "{word}" - {best_counter}{best_spesial_sign} Jackpot!')
        elif best_counter >= 6:
            print(f'ticket "{word}" - {best_counter}{best_spesial_sign}')
        else:
            print(f'ticket "{word}" - no match')
    else:
        print(f'ticket "{word}" - no match')

    counter = 0
    best_counter = 0
    spesial_sign = ""
    best_spesial_sign = ""
    count = 0
    best_count = 0
    spesial_s = ""
    best_special_s = ""



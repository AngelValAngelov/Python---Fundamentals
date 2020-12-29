def solve(let_dig):
    letters = []
    digits = []

    for i in letters_digits:
        if i.isdigit():
            digits.append(i)
        else:
            letters.append(i)

    take_list = []
    skip_list = []

    for i in range(len(digits)):
        if i % 2 == 0:
            take_list.append(digits[i])
        else:
            skip_list.append(digits[i])

    new_list = []

    for i in range(len(take_list)):
        new_list.append(letters[0:int(take_list[i])])
        del letters[0:int(take_list[i])]
        del letters[0:int(skip_list[i])]

    final = []
    for l in new_list:
        final.extend(l)
    final = "".join(final)

    print(final)


letters_digits = input()

solve(letters_digits)

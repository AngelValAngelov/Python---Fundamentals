def message(list_number, str_letters):
    list_num = []
    list_final = []

    for i in list_number:
        summm = 0
        for j in i:
            summm += int(j)
        list_num.append(summm)

    for number in list_num:
        number = int(number)
        if len(str_letters) > number:
            list_final.append(str_letters[number])
            str_letters = str_letters[:number] + str_letters[(number + 1):]
        else:
            number -= len(str_letters)
            list_final.append(str_letters[number])
            str_letters = str_letters[:number] + str_letters[(number + 1):]

    final = "".join(list_final)

    return final


list_numberr = input().split(" ")
str_letterss = input()

print(message(list_numberr, str_letterss))

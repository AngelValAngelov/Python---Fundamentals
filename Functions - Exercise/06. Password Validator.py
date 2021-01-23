def solve():
    alnum = True
    digit_counter = 0
    for letter in password:
        if letter.isalnum():
            continue
        else:
            alnum = False
            break
    for letter in password:
        all_digits = letter
        if all_digits.isdigit():
            digit_counter += 1

    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
    if not alnum:
        print("Password must consist only of letters and digits")
    if digit_counter < 2:
        print("Password must have at least 2 digits")
    if (6 <= len(password) <= 10) and alnum == True and digit_counter >= 2:
        print("Password is valid")


password = input()
password_length = len(password)

solve()

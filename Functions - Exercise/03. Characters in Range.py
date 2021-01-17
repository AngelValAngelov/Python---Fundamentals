char_one = input()
char_two = input()

def solve():
    missin = []
    for letter in range(ord(char_one) + 1,ord(char_two)):
        missin.append(chr(letter))

    str_missin = " ".join(missin)

    print(str_missin)


solve()
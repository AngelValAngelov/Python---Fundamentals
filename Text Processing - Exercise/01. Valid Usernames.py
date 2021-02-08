string = input().split(", ")
is_true = True

for word in string:
    if 3 <= len(word) <= 16:
        for ch in word:
            if not(ch.isnumeric() or ch.isalpha() or ch == "-" or ch == "_"):
                is_true = False
                break
            else:
                is_true = True
        if is_true:
            print(word)
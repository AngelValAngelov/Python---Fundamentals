def solve(sentences):
    new_list = []

    for word in sentences:
        num = [num for num in word if num.isdigit()]
        num = chr(int("".join(num)))
        letters = [lett for lett in word if lett.isalpha()]
        letters[0], letters[-1] = letters[-1], letters[0]
        letters = "".join(letters)
        new_list.append(num + letters)

    final_str = " ".join(new_list)
    print(final_str)


sen = input().split(" ")
solve(sen)

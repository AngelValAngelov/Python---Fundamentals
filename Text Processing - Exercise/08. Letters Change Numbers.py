text = input().split()
list_result = []
result = None

for word in text:
    result = 0
    first_letter = int(ord(word[0]))
    second_word = int(ord(word[-1]))
    number = int(word[1:-1])
    if word[0].isupper():
        first_letter -= 64
        result = number / first_letter
    else:
        first_letter -= 96
        result = number * first_letter

    if word[-1].isupper():
        second_word -= 64
        result -= second_word
    else:
        second_word -= 96
        result += second_word

    list_result.append(result)

final_sum = 0

for number in list_result:
    final_sum += float(number)

print(f"{final_sum:.2f}")




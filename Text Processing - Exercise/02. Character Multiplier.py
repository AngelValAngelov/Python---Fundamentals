string = input().split()

first_word = len(string[0])
second_word = len(string[1])
small_word = second_word
big_word = first_word

if first_word < second_word:
    small_word = first_word
    big_word = second_word
result = 0

word_1 = string[0]
word_2 = string[1]
for i in range(0 , small_word):
    result += ord(word_1[i]) * ord(word_2[i])

if small_word == len(word_1):
    for i in range(small_word, big_word):
        result += ord(word_2[i])
else:
    for i in range(small_word, big_word):
        result += (ord(word_1[i]))

print(result)





palindrome_list = []
words = input().split()
w = input()


def is_palindrome(word):
    global palindrome_list
    reversed_word = word[::-1]
    if word == reversed_word:
        palindrome_list.append(word)
    return palindrome_list


def palindrome_count(word):
    global palindrome_list
    count = 0
    for i in palindrome_list:
        if i == word:
            count += 1

    return f"Found palindrome {count} times"


def solve():
    for i in words:
        is_palindrome(i)

    return palindrome_list


print(solve())
print(palindrome_count(w))

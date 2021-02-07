import re


pattern = r"\d+"
text = input()
while text:
    numbers = re.findall(pattern, text)

    for num in numbers:
        print(num, end=" ")

    text = input()
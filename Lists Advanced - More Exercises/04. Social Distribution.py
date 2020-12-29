numbers = list(map(int, input().split(", ")))
min_money = int(input())

if sum(numbers) / len(numbers) < min_money:
    print("No equal distribution possible")

    exit()

for i in range(len(numbers)):
    if numbers[i] < min_money:
        diff = min_money - numbers[i]
        numbers[i] = min_money
        index = numbers.index(max(numbers))
        numbers[index] -= diff

print(numbers)

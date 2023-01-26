import re

text = input()
pattern = r'#[A-Za-z|A-Za-z\s]+#[0-9]{2}/[0-9]{2}/[0-9]{2}[#][0-9]+#|\|[A-Za-z|A-Za-z\s]+\|[0-9]{2}/[0-9]{2}/[0-9]{2}\|[0-9]+\|'
food_info = re.findall(pattern, text)

all_products = []
all_calories = 0
days_with_current_food = 0

for info in food_info:
    n = re.split(r"\#+|\|+", info)

    if int(n[-2]) <= 10000 or int(n[-2]) > 0:
        # if n[1] in all_products:

        all_products.append(n[1:-1])
print(all_products)
for c in all_products:
    all_calories += int(c[-1])

print(f"You have food to last you for: {all_calories // 2000} days!")


for food in all_products:
    food_type = food[0]
    date = food[1]
    nutrition = food[2]
    print(f"Item: {food_type}, Best before: {date}, Nutrition: {nutrition}")


































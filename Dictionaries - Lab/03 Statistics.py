product = input().split(": ")

items = {}

while product[0] != "statistics":
    key = product[0]
    value = product[1]
    if key not in items:
        items[key] = int(value)
    else:
        items[key] += int(value)
    product = input().split(": ")

print("Products in stock:")
product, quantity = items.keys(), items.values()
for product, quantity in items.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(items.keys())}")
print(f"Total Quantity: {sum(items.values())}")




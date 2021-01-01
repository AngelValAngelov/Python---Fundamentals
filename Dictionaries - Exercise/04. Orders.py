products = input().split()

items_key = {}
items_quantity = {}

while products[0] != "buy":
    item = products[0]
    price = float(products[1])
    quantity = float(products[2])
    if item not in items_key:
        items_key[item] = price
    elif item in items_key:
        items_key[item] = price
    if item not in items_quantity:
        items_quantity[item] = quantity
    else:
        items_quantity[item] += quantity
    products = input().split()


dea = {}

for k, v in items_key.items():
    print(f"{k} -> {(v * items_quantity[k]):.2f}")


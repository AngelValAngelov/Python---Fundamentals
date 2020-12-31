list_products = input().split()
products = input().split()
all_products = {}
for i in range(0, len(list_products), 2):
    key = list_products[i]
    value = int(list_products[i + 1])
    all_products[key] = value

for product in products:
    if product in all_products:
        print(f"We have {all_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

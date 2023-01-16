price_without_taxes = 0
price_with_taxes = 0
tax = 0.20
discount = 0.10
command = input()
total_amount_taxes = 0


while command != 'special' and command != 'regular':
    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total_amount_taxes = price + (price * tax)
        price_without_taxes += price
        price_with_taxes += total_amount_taxes

    command = input()

if price_with_taxes == 0:
    print("Invalid order!")
else:
    if command == 'special':
        total_amount_taxes = price_with_taxes - price_without_taxes
        price_with_taxes = price_with_taxes - price_with_taxes * discount
    else:
        total_amount_taxes = price_with_taxes - price_without_taxes


    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")


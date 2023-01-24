import re

orders = input()
pattern = r'%(?P<name>[A-Z]{1}[a-z]+)%[^|$%.]*<(?P<product>[A-Za-z0-9_]+)>([^|$%.])*\|(?P<count>[0-9]+)\|([|$%.a-zA-Z]*)(?P<price>([0-9]+)\.?[0-9]+)\$'

total_income = 0

while orders != 'end of shift':
    matches = re.finditer(pattern, orders)
    for match in matches:
        total_income += int(match.group('count')) * float(match.group('price'))
        current_income = int(match.group('count')) * float(match.group('price'))
        print(f"{match.group('name')}: {match.group('product')} - {current_income:.2f}")

    orders = input()

print(f'Total income: {total_income:.2f}')

import re

text = input()
pattern = r'=[A-Z][A-Za-z]{2,}=|/[A-Z][A-Za-z]{2,}/'

cities = re.findall(pattern, text)
points = sum([len(c) for c in cities]) - len(cities) * 2
print(f"Destinations: {', '.join([c[1:-1] for c in cities])}")
print(f"Travel Points: {points}")


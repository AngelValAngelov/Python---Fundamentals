import re

dates = input()

pattern = r'[0-9]{2}/[A-Z][a-z]{2}/[0-9]{4}|[0-9]{2}-[A-Z][a-z]{2}-[0-9]{4}|[0-9]{2}\.[A-Z][a-z]{2}\.[0-9]{4}'
result = re.findall(pattern, dates)

for date in result:
    day = date[0:2]
    month = date[3:6]
    year = date[7:11]
    print(f'Day: {day}, Month: {month}, Year: {year}')

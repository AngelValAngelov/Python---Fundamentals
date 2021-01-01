firm = input().split(" -> ")

list_company = {}

while firm[0] != "End":
    company = firm[0]
    name = firm[1]
    if company not in list_company:
        list_company[company] = []
        if name not in company:
            list_company[company].append(name)
    else:
        if name not in list_company[company]:
            list_company[company].append(name)
    firm = input().split(" -> ")

sorted_dict = dict(sorted(list_company.items()))

for key, value in sorted_dict.items():
    print(key)
    for name in value:
        print(f"-- {name}")

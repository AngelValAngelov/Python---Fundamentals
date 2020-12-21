first_list = input().split(", ")
second_list = input().split(", ")

final_list = []

for i in first_list:
    for j in second_list:
        if i in j:
            if i in final_list:
                continue
            else:
                final_list.append(i)

print(final_list)

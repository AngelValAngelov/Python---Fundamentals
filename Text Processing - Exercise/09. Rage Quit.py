from collections import OrderedDict

string = input().upper()
new_string = ""
counter = ""
s = ""

for i in range(len(string)):
    if string[i].isnumeric():
        counter += string[i]
        if i != len(string) - 1:
            if string[i + 1].isdigit():
                continue
    else:
        s += string[i]

    if counter != "":
        new_string += (s * int(counter))

        counter = ""
        s = ""

n_s = "".join(OrderedDict.fromkeys(new_string))
print(f"Unique symbols used: {len(n_s)}")
print(new_string)

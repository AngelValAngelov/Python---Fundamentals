file = input().split("\\")

last_part = file[-1]
last_part = last_part.split(".")

print(f"File name: {last_part[0]}")
print(f"File extension: {last_part[1]}")
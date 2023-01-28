employees = sum([int(input()) for e in range(3)])
students_count = int(input())
hours = 0
break_time = 0

while students_count > 0:
    break_time += 1
    if break_time < 4:
        students_count -= employees
    else:
        break_time = 0
    hours += 1

print(f'Time needed: {hours}h.')

def office_chairs(num):
    is_true = False
    room = 0
    chairs_left = 0
    while num > 0:
        chairs = input().split()
        room += 1
        if len(chairs[0]) >= int(chairs[1]):
            chairs_left += len(chairs[0]) - int(chairs[1])
        else:
            chairs_needed = abs(len(chairs[0]) - int(chairs[1]))
            print(f"{chairs_needed} more chairs needed in room {room}")
            is_true = True
        num -= 1

    if not is_true:
        print(f"Game On, {chairs_left} free chairs left")


number = int(input())

office_chairs(number)

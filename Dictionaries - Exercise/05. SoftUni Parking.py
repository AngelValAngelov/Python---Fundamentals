commands = int(input())

registred_cars = {}

while commands != 0:
    registrator = input().split()
    register_unregister = registrator[0]
    name = registrator[1]
    if name in registred_cars.keys() and register_unregister == "register":
        print(f"ERROR: already registered with plate number {registrator[2]}")
    elif name not in registred_cars.keys() and register_unregister == "register":
        registred_cars[name] = registrator[2]
        print(f"{name} registered {registrator[2]} successfully")
    elif name not in registred_cars.keys() and register_unregister == "unregister":
        print(f"ERROR: user {name} not found")
    else:
        del registred_cars[name]
        print(f"{name} unregistered successfully")
    commands -= 1

for key, value in registred_cars.items():
    print(f"{key} => {value}")
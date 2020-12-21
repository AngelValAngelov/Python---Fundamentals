def solve(version):
    if int(version[-1]) < 9:
        version[-1] = str(int(version[-1]) + 1)
    elif int(version[-2]) == 9 and int(version[-1]) == 9:
        version[0] = str(int(version[0]) + 1)
        version[-1] = str(int(0))
        version[-2] = str(int(0))
    elif int(version[-1]) == 9:
        version[-2] = str(int(version[-2]) + 1)
        version[-1] = str(int(0))
    return ".".join(version)


vers = input().split(".")

print(solve(vers))
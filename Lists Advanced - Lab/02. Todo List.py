todo = []
note = input()


def solve():
    global todo, note
    while note != "End":
        note = note.split("-")
        index = int(note[0])
        text = note[1]
        todo.insert(index, (index, text))

        note = input()
    return sorted(todo)


result = []

for i in solve():
    result.append(i[1])

print(result)

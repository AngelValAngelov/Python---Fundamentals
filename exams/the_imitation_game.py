def move_command(instructions, message):
    command = instructions[0]
    index = int(instructions[1])
    substring = message[index:]
    message = message.replace(substring, '')
    return substring + message


def insert_numbers(instructions, message):
    command = instructions[0]
    index = int(instructions[1])
    value = instructions[2]
    return message[:index] + value + message[index:]


def change_string(instructions, message):
    command = instructions[0]
    substring = instructions[1]
    replacement_substring = instructions[2]
    return message.replace(substring, replacement_substring)


message = input()
instructions = list(map(str, input().split('|')))

while len(instructions) != 1:
    if instructions[0] == 'Move':
        message = move_command(instructions, message)
    elif instructions[0] == 'Insert':
        message = insert_numbers(instructions, message)
    elif instructions[0] == 'ChangeAll':
        message = change_string(instructions, message)
    instructions = list(map(str, input().split('|')))

print(f"The decrypted message is: {message}")

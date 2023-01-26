def add_piece(piece):
    command = piece[0]
    piece_name = piece[1]
    composer = piece[2]
    key = piece[3]
    if piece_name in pieces:
        print(f"{piece_name} is already in the collection!")
    else:
        pieces[piece_name] = piece[2:]
        print(f"{piece_name} by {composer} in {key} added to the collection!")


def remove_piece(piece):
    command = piece[0]
    piece_name = piece[1]
    if piece_name in pieces:
        pieces.pop(piece_name, None)
        print(f"Successfully removed {piece_name}!")
    else:
        print(f"Invalid operation! {piece_name} does not exist in the collection.")


def change_key(piece):
    command = piece[0]
    piece_name = piece[1]
    new_key = piece[2]
    if piece_name in pieces:
        pieces[piece_name][-1] = new_key
        print(f"Changed the key of {piece_name} to {new_key}!")
    else:
        print(f"Invalid operation! {piece_name} does not exist in the collection.")


number = int(input())
pieces = {}

for _ in range(number):
    piece = input().split('|')
    pieces[piece[0]] = piece[1:]

new_piece = input()
if new_piece != 'Stop':
    new_piece = new_piece.split('|')

while new_piece != 'Stop':
    command = new_piece[0]
    if command == 'Add':
        add_piece(new_piece)
    elif command == 'Remove':
        remove_piece(new_piece)
    elif command == 'ChangeKey':
        change_key(new_piece)

    new_piece = input()
    if new_piece != 'Stop':
        new_piece = new_piece.split('|')

for key, value in pieces.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")

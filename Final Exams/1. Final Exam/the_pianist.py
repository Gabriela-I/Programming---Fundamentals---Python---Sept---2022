def add(group, song, writer, tone):
    if song in group:
        print(f"{song} is already in the collection!")
    else:
        group[song] = [writer, tone]
        print(f"{song} by {writer} in {tone} added to the collection!")


def remove(group, song):
    if song not in group:
        print(f"Invalid operation! {song} does not exist in the collection.")
    else:
        del group[song]
        print(f"Successfully removed {song}!")


def change_key(group, song, tone):
    if song not in group:
        print(f'Invalid operation! {song} does not exist in the collection.')
    else:
        del group[song][1]
        group[song] += [tone]
        print(f"Changed the key of {song} to {tone}!")


number_of_pieces = int(input())
collection = {}
for num in range(number_of_pieces):
    piece, composer, key = input().split('|')
    collection[piece] = [composer, key]
command = input()
while command != 'Stop':
    if command == 'Stop':
        break
    info = command.split('|')
    current_command = info[0]
    if current_command == 'Add':
        piece, composer, key = info[1], info[2], info[3]
        add(collection, piece, composer, key)
    elif current_command == 'Remove':
        piece = info[1]
        remove(collection, piece)
    else:
        piece, new_key = info[1], info[2]
        change_key(collection, piece, new_key)
    command = input()

for key, value in collection.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")


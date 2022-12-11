def move(code, num_of_letters):
    code = code[num_of_letters:] + code[: num_of_letters]
    return code


def insert(code, place, some_value):
    code = code[:place] + some_value + code[place:]
    return code


def change_all(code, current_str, replacement_str):
    code = code.replace(current_str, replacement_str)
    return code


message = input()
while True:
    command = input().split('|')
    if command[0] == 'Decode':
        print(f"The decrypted message is: {message}")
        break
    elif command[0] == 'Move':
        letters = int(command[1])
        message = move(message, letters)
    elif command[0] == 'Insert':
        index, value = int(command[1]), command[2]
        message = insert(message, index, value)
    else:
        substring, replacement = command[1], command[2]
        message = change_all(message, substring, replacement)
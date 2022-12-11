text = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    commands = command.split(':|:')
    current_command, obj = commands[0], commands[1]
    if current_command != 'ChangeAll':
        if current_command == 'InsertSpace':
            text = text[:int(obj)] + ' ' + text[int(obj):]
            print(text)

        if current_command == 'Reverse':
            if obj in text:
                new_obj = obj[::-1]
                text = text.replace(obj, '', 1)
                text = text + new_obj
                print(text)
            else:
                print('error')
    else:
        replacement_text = commands[2]
        while obj in text:
            text = text.replace(obj, replacement_text)
        print(text)

print(f"You have a new text message: {text}")